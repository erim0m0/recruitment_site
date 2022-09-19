import redis

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.api.send_otp import send_otp
from accounts.api.serializers import (
    AuthenticationSerializer,
    OtpSerilizer, UsersListSerializer,
)
from config.settings import REDIS_PORT, REDIS_HOST_NAME


class UsersList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UsersListSerializer
    queryset = get_user_model().objects.all()


class Register(APIView):
    permission_classes = (AllowAny,)

    # throttle_classes = (ScopedRateThrottle,)
    # throttle_scope = "authentication"

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_phone = serializer.data.get("phone")

        is_exist_user: bool = get_user_model().objects.filter(phone=received_phone).values("phone").exists()
        if is_exist_user:
            return Response(
                {
                    "User exists.": "Please enter a different phone number."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return send_otp(received_phone)


class VerifyOtp(APIView):
    permission_classes = (AllowAny,)

    # throttle_classes = (ScopedRateThrottle,)
    # throttle_scope = "verify_authentication"

    def post(self, request):
        serializer = OtpSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_phone = serializer.data.get("phone")
        received_code = serializer.data.get("code")
        received_id_code = serializer.data.get("id_code")

        redis_conf = redis.Redis(host=REDIS_HOST_NAME, port=REDIS_PORT)
        data = redis_conf.hvals(received_phone)

        if received_id_code.encode() in data and received_code.encode() in data:
            user, created = get_user_model().objects.get_or_create(phone=received_phone)
            refresh = RefreshToken.for_user(user)
            redis_conf.delete(received_phone)

            context = {
                "created": created,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            return Response(
                context,
                status=status.HTTP_201_CREATED
            )

        else:
            redis_conf.hincrby(received_phone, 'retry', 1)
            if data[-1] == b'4':
                redis_conf.delete(received_phone)
                return Response(
                    {
                        "Send otp again": "Please send otp again",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {
                "Incorrect code.": "The code entered is incorrect.",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_phone = serializer.data.get("phone")

        is_exist_user: bool = get_user_model().objects.filter(phone=received_phone).values("phone").exists()
        if not is_exist_user:
            return Response(
                {
                    "No User exists.": "Please enter another phone number.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return send_otp(received_phone)

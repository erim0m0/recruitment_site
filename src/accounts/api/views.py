from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView

from accounts.api.send_otp_or_not import send_otp_or_not
from accounts.api.serializers import (
    AuthenticationSerializer,
    OtpSerilizer, UsersListSerializer,
)
from accounts.models.OTP_doc import OTPDocument


class UsersList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UsersListSerializer
    queryset = get_user_model().objects.all()


class Register(APIView):
    permission_classes = (AllowAny,)

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

        return send_otp_or_not(received_phone)


class VerifyOtp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = OtpSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_code = serializer.data.get('code')
        received_id_code = serializer.data.get('id_code')

        is_exist_id_code: bool = OTPDocument.objects.filter(id_code=received_id_code).values('id_code').exists()
        if is_exist_id_code:
            try:
                otp = OTPDocument.objects.get(code=received_code)

                is_expired_time: bool = (timezone.now() - timedelta(minutes=2)) > otp.create_at
                if not is_expired_time:
                    user, created = get_user_model().objects.get_or_create(phone=otp.contact)
                    refresh = RefreshToken.for_user(user)
                    otp.delete()
                    context = {
                        "created": created,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                    return Response(
                        context,
                        status=status.HTTP_200_OK
                    )
                else:
                    otp.delete()
                    return Response(
                        {
                            "Code expired.": "The entered code has expired.",
                        },
                        status=status.HTTP_408_REQUEST_TIMEOUT
                    )

            except ObjectDoesNotExist:
                obj = OTPDocument.objects.get(id_code=received_id_code)
                obj.retry += 1
                obj.save(update_fields=["retry"])

                if obj.retry > 4:
                    obj.delete()
                    return Response(
                        {
                            "Code expired.": "The entered code has expired.",
                        },
                        status=status.HTTP_408_REQUEST_TIMEOUT
                    )

                return Response(
                    {
                        "Incorrect code.": "The code entered is incorrect.",
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

        return Response(
            {
                "Incorrect code.": "The code entered is incorrect.",
            },
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_phone = serializer.data.get('phone')

        is_exist_user: bool = get_user_model().objects.filter(phone=received_phone).values("phone").exists()
        if not is_exist_user:
            return Response(
                {
                    "No User exists.": "Please enter another phone number.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return send_otp_or_not(received_phone)

from typing import List
from redis import Redis

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import ScopedRateThrottle

from accounts.api.otp_creator import send_otp
from accounts.models.blocked_phones import BlockedPhone
from config.settings import REDIS_PORT, REDIS_HOST_NAME
from accounts.api.serializers import (
    AuthenticationSerializer, OtpSerilizer, GetTwoStepPasswordSerializer,
    ChangeTwoStepPasswordSerializer
)


class Register(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "auth"

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_phone = serializer.data.get("phone")

        is_blocked: bool = BlockedPhone.objects.filter(phone=received_phone).exists()
        if is_blocked:
            return Response(
                {
                    "User exists.": "Please enter a different phone number."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        data_filter = {
            "phone": received_phone
        }
        if "operator" in request.path:
            data_filter["is_operator"] = True

        is_exist_user: bool = get_user_model().objects.filter(**data_filter).exists()
        if is_exist_user:
            return Response(
                {
                    "User exists.": "Please enter a different phone number."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return send_otp(received_phone)


class VerifyOtp(APIView):
    #throttle_classes = [ScopedRateThrottle]
    #throttle_scope = "verify_authentication"

    def post(self, request):
        serializer = OtpSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_phone = serializer.data.get("phone")
        received_code = serializer.data.get("code")
        received_id_code = serializer.data.get("id_code")

        _redis_conf = Redis(host=REDIS_HOST_NAME, port=REDIS_PORT)
        data: List = _redis_conf.hvals(received_phone)
        if all((received_id_code.encode() in data, received_code.encode() in data)):
            operator_data = dict()

            if "operator" in request.path:
                operator_data.update({"is_operator": True})

            user, created = get_user_model().objects.update_or_create(
                phone=received_phone,
                defaults=operator_data
            )

            refresh = RefreshToken.for_user(user)
            context = {
                "created": created,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            _redis_conf.delete(received_phone)

            return Response(
                context,
                status=status.HTTP_201_CREATED
            )

        else:
            _redis_conf.hincrby(received_phone, "retry", 1)
            try:
                if data[-1] == b'4':
                    _redis_conf.delete(received_phone)
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
            except IndexError:
                return Response(
                    {
                        "Send otp again": "Please send otp again",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )


class Login(APIView):

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        received_phone = serializer.data.get("phone")

        data_filter = {
            "phone": received_phone,
        }

        if "operator" in request.path:
            data_filter.update({"is_operator": True})

        is_exist_user: bool = get_user_model().objects.filter(**data_filter).exists()
        if not is_exist_user:
            return Response(
                {
                    "No User exists.": "Please enter another phone number.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return send_otp(received_phone)


class DeleteAccount(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def delete(self, request):
        user = get_user_model().objects.get(pk=request.user.username)
        user.delete()
        return Response(
            {
                "Removed successfully.": "Your account has been successfully deleted."
            },
            status=status.HTTP_204_NO_CONTENT
        )


class CreateTwoStepPassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GetTwoStepPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recieved_password = serializer.get("password")

        user = get_object_or_404(
            get_user_model(),
            pk=request.user.pk
        )
        user.set_password(recieved_password)
        user.save(update_fields=["password"])

        return Response(
            {
                "Successful.": "Your password was changed successfully.",
            },
            status=status.HTTP_200_OK,
        )


class VerifyTwoStepPassword(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "verify_authentication"

    def post(self, request):
        serializer = GetTwoStepPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recieved_password = serializer.get("password")

        user = get_object_or_404(
            get_user_model(),
            pk=request.user.username
        )
        check_password: bool = user.check_password(recieved_password)
        if check_password:
            refresh = RefreshToken.for_user(user)
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
            return Response(
                {
                    "Error!": "The password entered is incorrect",
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )


class ChangeTwoStepPassword(APIView):
    """
    post:
        Send a password to change a two-step-password.

        parameters: [old_password, new_password, confirm_new_password,]
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangeTwoStepPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_password = serializer.data.get("old_password")
        user = get_object_or_404(
            get_user_model(),
            pk=request.user.pk,
        )
        check_password: bool = user.check_password(old_password)

        if check_password:
            new_password = serializer.data.get("password")
            user.set_password(new_password)
            user.save(update_fields=["password"])

            return Response(
                {
                    "Successful.": "Your password was changed successfully.",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "Error!": "The password entered is incorrect.",
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

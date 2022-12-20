from rest_framework import serializers

from django.contrib.auth import get_user_model

from accounts.models.company import CompanyProfile
from accounts.models.user_profile import (
    Profile
)


########## AUTHENTICATION'S SERIALIZERS ##########

class AuthenticationSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=10,
        min_length=10
    )

    def validate_phone(self, value):
        from re import match

        if not match("^9\d{2}\s*?\d{3}\s*?\d{4}$", value):
            raise serializers.ValidationError(
                {
                    "Error": "The phone number is Invalid."
                }
            )
        return value


class OtpSerilizer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=10,
        min_length=10
    )

    code = serializers.CharField(
        max_length=6,
    )

    id_code = serializers.CharField(
        max_length=32,
        min_length=32
    )

    def validate_code(self, value):
        try:
            int(value)
        except ValueError:
            raise serializers.ValidationError(
                {
                    "Error": "code is Invalid."
                }
            )
        return value


class GetTwoStepPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=20
    )
    confirm_password = serializers.CharField(
        max_length=20
    )

    def validate_password(self, value):
        from re import match

        if not match(
                "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&-+=()])(?=\\S+$).{8, 20}$",
                value):
            raise serializers.ValidationError(
                {"Error": "The phone number is Invalid."}
            )
        return value

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError(
                {"Error": "Your passwords didn't match."}
            )
        return data


class ChangeTwoStepPasswordSerializer(GetTwoStepPasswordSerializer):
    old_password = serializers.CharField(
        max_length=20
    )


########## PROFILE SERIALIZERS ##########

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = [
            "id", "user", "slug"
        ]


class ProfileCreateSerializer(serializers.ModelSerializer):
    class meta:
        model = Profile
        fields = "__all__"


########## COMPANY'S SERIALIZERS ##########

class CompaniesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = [
            "id", "name", "logo"
        ]


class CompanyProfileSerializer(serializers.ModelSerializer):
    organizational_interface_phone = serializers.CharField(
        source="organizational_interface.phone"
    )

    class Meta:
        model = CompanyProfile
        exclude = [
            "created_at",
            "organizational_interface"
        ]


class CompanyProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        exclude = [
            "created_at",
            "number_of_advertisements",
            "organizational_interface"
        ]

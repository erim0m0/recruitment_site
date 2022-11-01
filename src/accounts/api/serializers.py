from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models.user_profile import (
    Profile,
    AboutMe,
    WorkExperience,
    EducationalRecord,
    PersonalInformation
)
from accounts.models.company import CompanyProfile


########## Authentication Serializers ##########

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
        min_length=6
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
                    "error": "code is Invalid."
                }
            )
        return value


########## Profiles Serializers ##########

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("user", "id", "slug")


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        exclude = ("user", "id", "slug")


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        exclude = ("user", "id", "slug")


class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        exclude = ("user", "id", "slug")


class EducationalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalRecord
        exclude = ("user", "id", "slug")


########## Company ##########

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        exclude = [
            "create_at"
        ]

class CompanyProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        exclude = [
            "create_at",
            "number_of_advertisements",
            "organizational_interface"
        ]

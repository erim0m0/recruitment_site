from rest_framework import serializers
from django.contrib.auth import get_user_model


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id", "phone",
            "date_joined"
        )


class AuthenticationSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=10,
        min_length=10
    )

    def validate_phone(self, value):
        from re import match

        if not match("^9\d{2}\s*?\d{3}\s*?\d{4}$", value):
            raise serializers.ValidationError("The phone number is Invalid.")
        return value


class OtpSerilizer(serializers.Serializer):
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
            raise serializers.ValidationError({
                "error": "code is Invalid."
            })
        return value

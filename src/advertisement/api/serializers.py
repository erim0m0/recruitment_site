from rest_framework import serializers
from advertisement.models import Advertisement
from rest_framework.serializers import ModelSerializer


class AdvertisementsListSerializer(ModelSerializer):
    company__name = serializers.CharField(
        max_length=120
    )

    class Meta:
        model = Advertisement
        fields = [
            "id",
            "title",
            "city",
            "company__name"
        ]


class AdvertisementSerializer(ModelSerializer):
    company_name = serializers.CharField(
        source="company.name", read_only=True
    )

    class Meta:
        model = Advertisement
        exclude = [
            "company"
        ]


class AdvertisementCreateSerializer(ModelSerializer):
    company_name = serializers.CharField(
        source="company.name", read_only=True
    )

    class Meta:
        model = Advertisement
        exclude = [
            "company"
        ]

from rest_framework.serializers import Serializer, ModelSerializer
from advertisement.models import Advertisement
from rest_framework import serializers


class AdvertisementsListSerializer(ModelSerializer):
    company__name = serializers.CharField(
        max_length=120
    )

    class Meta:
        model = Advertisement
        fields = [
            "title",
            "city",
            "company__name"
        ]


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        exclude = [
            "is_show_salary",
            "is_unknown"
        ]


class AdvertisementCreateSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        exclude = [
            "company"
        ]

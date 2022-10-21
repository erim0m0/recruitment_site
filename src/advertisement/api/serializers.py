from rest_framework.serializers import Serializer, ModelSerializer
from advertisement.models import Advertisement


class AdvertisementsListSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            "title",
            ""
        ]

class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"



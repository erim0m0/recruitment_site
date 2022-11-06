from typing import Dict

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
    IsAuthenticated
)

from ..models import Advertisement
from accounts.models.company import CompanyProfile
from permissions import (
    IsFounderOrStaff,
    IsOperatorOrNot,
    IsCompanyExistOrNot
)
from .serializers import (
    AdvertisementsListSerializer,
    AdvertisementSerializer,
    AdvertisementCreateSerializer
)


class AdertisementsList(ListAPIView):
    permission_classes = [
        AllowAny
    ]
    serializer_class = AdvertisementsListSerializer
    filterset_fields = [
        "title",
        "city",
    ]
    search_fields = [
        "company__name",
    ]

    def get_queryset(self):
        queryset = Advertisement.objects.values(
            "title", "city", "company__name"
        )
        return queryset


class AdvertisementView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [
        IsFounderOrStaff
    ]

    # TODO: add a feature for is_known field from company's profile
    def get_object(self):
        obj = get_object_or_404(
            Advertisement.objects.select_related("company"),
            pk=self.kwargs["pk"]
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def show_data(self) -> Dict:
        instance = self.get_object()
        company_field = instance.company

        serializer = self.get_serializer(instance)
        serializer_data: Dict = serializer.data
        serializer_data["company"] = company_field.name
        return serializer_data

    def retrieve(self, request, *args, **kwargs):
        result: Dict = self.show_data()
        return Response(
            result,
            status=status.HTTP_200_OK
        )


class AdvertisementCreateView(CreateAPIView):
    serializer_class = AdvertisementCreateSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsOperatorOrNot,
        IsCompanyExistOrNot
    ]

    def perform_create(self, serializer):
        wanted_company = CompanyProfile.objects.only(
            "number_of_advertisements"
        ).get(
            organizational_interface=self.request.user
        )
        wanted_company.number_of_advertisements += 1
        wanted_company.save(
            update_fields=["number_of_advertisements"]
        )
        return serializer.save(
            company=wanted_company
        )

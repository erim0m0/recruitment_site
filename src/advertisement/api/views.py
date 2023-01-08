from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
)

from advertisement.models import Advertisement
from accounts.models.company import CompanyProfile
from permissions import (
    IsFounderOrStaff, IsOperatorOrNot, IsCompanyExistOrNot
)
from .serializers import (
    AdvertisementsListSerializer, AdvertisementSerializer, AdvertisementCreateSerializer
)


class AdertisementsList(ListAPIView):
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
            "id", "title", "city", "company__name"
        )
        return queryset


class AdvertisementDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [
        IsFounderOrStaff
    ]

    def get_object(self):
        obj = get_object_or_404(
            Advertisement.objects.select_related("company"),
            pk=self.kwargs["pk"]
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def delete(self, request, *args, **kwargs):
        try:
            wanted_company = CompanyProfile.objects.only(
                "number_of_ad"
            ).get(
                operator=self.request.user.pk
            )
            wanted_company.number_of_ad -= 1
            wanted_company.save(
                update_fields=["number_of_ad"]
            )
        except Exception:
            pass
        return super().delete(request, *args, **kwargs)


class AdvertisementCreateView(CreateAPIView):
    serializer_class = AdvertisementCreateSerializer
    permission_classes = [
        IsOperatorOrNot,
        IsCompanyExistOrNot
    ]

    def perform_create(self, serializer):
        wanted_company = CompanyProfile.objects.only(
            "number_of_ad"
        ).get(
            operator=self.request.user.pk
        )
        wanted_company.number_of_ad += 1
        wanted_company.save(
            update_fields=["number_of_ad"]
        )
        return serializer.save(
            company=wanted_company
        )

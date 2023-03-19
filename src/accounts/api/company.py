from typing import List, Dict

from rest_framework.generics import (
    UpdateAPIView, CreateAPIView, RetrieveDestroyAPIView, ListAPIView,
)

from django.shortcuts import get_object_or_404

from accounts.api import serializers
from accounts.models.company import CompanyProfile
from permissions import IsOperatorOrStaff, IsOperatorOrNot


class CompaniesList(ListAPIView):
    serializer_class = serializers.CompaniesListSerializer

    def get_queryset(self):
        return CompanyProfile.objects.only("name", "logo")


class CompanyProfileDetailDestroy(RetrieveDestroyAPIView):
    serializer_class = serializers.CompanyProfileSerializer
    permission_classes = [IsOperatorOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            CompanyProfile.objects.defer(
                "created_at",
                "number_of_ad"
            ).select_related(
                "operator"
            ), pk=self.kwargs.get("pk")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


class CompanyProfileUpdate(UpdateAPIView):
    serializer_class = serializers.CompanyProfileCreateSerializer
    permission_classes = [IsOperatorOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            CompanyProfile.objects.defer(
                "created_at",
                "operator",
                "number_of_ad"
            ), pk=self.kwargs.get("pk")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


class CompanyProfileCreate(CreateAPIView):
    serializer_class = serializers.CompanyProfileCreateSerializer
    permission_classes = [IsOperatorOrNot]

    def perform_create(self, serializer):
        serializer.save(
            operator=self.request.user
        )

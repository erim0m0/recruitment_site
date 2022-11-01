from typing import List, Dict

from rest_framework import status
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from accounts.api.serializers import (
    CompanyProfileSerializer,
    CompanyProfileCreateSerializer
)
from permissions import IsOperatorOrStaff
from accounts.models.company import CompanyProfile


class CompanyProfileAPIViews(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileSerializer

    permission_classes = [IsOperatorOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            CompanyProfile.objects.defer(
                "create_at",
            ).select_related(
                "industry",
                "organizational_interface"
            ), pk=self.kwargs.get("pk")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def show_data(self) -> Dict:
        instance = self.get_object()
        operator = instance.organizational_interface
        industry = instance.industry

        serializer = self.get_serializer(instance)
        serializer_data: Dict = serializer.data

        try:
            serializer_data["industry"] = industry.type
        except AttributeError:
            pass
        finally:
            try:
                serializer_data["organizational_interface"] = operator.phone
            except AttributeError:
                pass

        return serializer_data

    def retrieve(self, request, *args, **kwargs):
        result: Dict = self.show_data()
        return Response(
            result,
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        main_update = super(CompanyProfileAPIViews, self).update(request, *args, **kwargs)
        result: Dict = self.show_data()
        return Response(
            result,
            status=status.HTTP_200_OK
        )
    # Todo: Add permisions from opeartor -> company_profile
    def post(self, request, *args, **kwargs):
        serializer = CompanyProfileCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            organizational_interface=request.user
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

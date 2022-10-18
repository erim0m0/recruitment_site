from redis import Redis
from typing import List, Dict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from accounts.api.serializers import (
    OrganizationalInterfaceSerializer,
    CompanyProfileSerializer,
    AuthenticationSerializer
)
from permissions import IsStaffOrOwner, IsSuperUserOrReadOnly
from accounts.models.company import OrganizationalInterface, CompanyProfile


class OperatorProfile(RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizationalInterfaceSerializer

    # TODO: edit the permission
    permission_classes = (IsStaffOrOwner,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data_serializer: Dict = self.get_serializer(instance).data
        data_serializer.pop("password")
        return Response(data_serializer)

    def perform_update(self, serializer):
        received_password = serializer.validated_data.get("phone")
        hash_pass = make_password(received_password)
        return serializer.save(
            password=hash_pass
        )

    def get_object(self):
        operator_user = get_object_or_404(
            OrganizationalInterface,
            phone=self.kwargs["slug"]
        )
        return operator_user


class CompanyProfileRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileSerializer

    # TODO: edit the setting of permission
    permission_classes = (IsStaffOrOwner,)

    def get_object(self):
        obj = get_object_or_404(
            CompanyProfile,
            pk=self.kwargs["pk"]
        )
        return obj

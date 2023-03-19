from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError
from rest_framework.generics import (
    CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)

from accounts.api import serializers
from permissions import IsUserOrStaff
from accounts.models import user_profile


# PROFILE'S VIEW

class CreateProfile(CreateAPIView):
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsUserOrStaff]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsUserOrStaff]
    lookup_field = "phone"

    def get_object(self):
        obj = get_object_or_404(
            user_profile.Profile.objects.defer(
                "user"
            ),
            user__phone=self.kwargs.get("phone")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


# WORK EXPERIENCE'S VIEW

class CreateWorkExperience(ListCreateAPIView):
    serializer_class = serializers.WorkExperienceSerializer
    permission_classes = [IsUserOrStaff]
    search_fields = [
        "user__phone",
    ]

    def get_queryset(self):
        return user_profile.WorkExperience.objects.defer("user")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response(
                {"Not Created!": "Try again!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class WorkExperienceView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WorkExperienceSerializer
    permission_classes = [IsUserOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            user_profile.WorkExperience.objects.defer("user"),
            pk=self.kwargs.get("pk")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


# Educational Record'S VIEW


class CreateEducationalRecord(ListCreateAPIView):
    serializer_class = serializers.EducationalRecordSerializer
    permission_classes = [IsUserOrStaff]
    search_fields = [
        "user__phone",
    ]

    def get_queryset(self):
        return user_profile.EducationalRecord.objects.defer("user")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response(
                {"Not Created!": "Try again!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class EducationalRecordView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EducationalRecordSerializer
    permission_classes = [IsUserOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            user_profile.EducationalRecord.objects.defer("user"),
            pk=self.kwargs.get("pk")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

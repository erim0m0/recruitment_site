from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404
from .serializers import (
    ProfileSerializer,
    WorkExperienceSerializer,
    EducationalRecordSerializer,
    CVSerializer
)

from permissions import IsSuperUserOrReadOnly, IsOperatorOrStaff, IsUserOrStaff
from accounts.models.user_profile import (
    Profile,
    WorkExperience,
    EducationalRecord,
    CV
)


class ProfileDetailUpdate(RetrieveUpdateAPIView):
    # permission_classes = [
    #     IsAuthenticated,
    #     IsUserOrStaff,
    # ]
    lookup_field = "slug"

    def get_serializer_class(self):
        serializers = {
            "work-experience": "WorkExperienceSerializer",
            "educational-record": "EducationalRecordSerializer",
            "cv": "CVSerializer"
        }

        try:
            profile = self.kwargs["profile"]
            serializer_class = eval(serializers[profile])
        except KeyError:
            serializer_class = ProfileSerializer

        return serializer_class

    def get_object(self):
        obj = get_object_or_404(
            Profile.objects.defer(
                "user", "id", "slug"
            ),
            slug=self.kwargs["slug"]
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

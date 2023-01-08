from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404

from permissions import IsUserOrStaff
from accounts.models.user_profile import Profile, WorkExperience, EducationalRecord
from .serializers import ProfileSerializer, WorkExperienceSerializer, EducationalRecordSerializer


class ProfileView(RetrieveUpdateAPIView, CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsUserOrStaff]
    lookup_field = "slug"

    def get_object(self):
        obj = get_object_or_404(
            Profile.objects.defer(
                "id", "slug", "user"
            ),
            slug=self.kwargs.get("slug")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            slug=self.request.user.phone
        )


class WorkExperienceView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsUserOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            WorkExperience.objects.defer("user"),
            user__phone=self.kwargs.get("slug")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class EducationalRecordView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    serializer_class = EducationalRecordSerializer
    permission_classes = [IsUserOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            EducationalRecord.objects.defer("user"),
            user__phone=self.kwargs.get("slug")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

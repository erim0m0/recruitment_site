from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from django.shortcuts import get_object_or_404

from accounts.models.user_profile import Profile
from permissions import IsOperatorOrNot, IsUserOrStaff
from .serializers import ProfileSerializer, ProfileCreateSerializer


class ProfileDetailUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [
        IsOperatorOrNot,
        IsUserOrStaff
    ]
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(
            Profile.objects.defer(
                "id", "slug", "user"
            ),
            slug=slug
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

class ProfileCreate(CreateAPIView):
    serializer_class = ProfileCreateSerializer
    permission_classes = [
        IsOperatorOrNot
    ]
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        return serializer.save(
            user = self.request.user,
            slug = self.request.user.phone
        )
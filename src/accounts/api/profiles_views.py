from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404
from .serializers import (
    ProfileSerializer,
    AboutMeSerializer,
    PersonalInformationSerializer,
    WorkExperienceSerializer,
    EducationalRecordSerializer
)

from permissions import IsSuperUserOrReadOnly, IsOperatorOrStaff, IsUserOrStaff
from accounts.models.user_profile import (
    Profile,
    AboutMe,
    WorkExperience,
    PersonalInformation,
    EducationalRecord
)

dict_conf = {
    "p": ("ProfileSerializer", "Profile"),
    "pi": ("PersonalInformationSerializer", "PersonalInformation"),
    "am": ("AboutMeSerializer", "AboutMe"),
    "we": ("WorkExperienceSerializer", "WorkExperience"),
    "er": ("EducationalRecordSerializer", "EducationalRecord")
}


class ProfileDetailUpdate(RetrieveUpdateAPIView):
    permission_classes = (
        IsAuthenticated,
        IsUserOrStaff,
    )
    lookup_field = "slug"

    def dispatch(self, request, *args, **kwargs):
        if self.kwargs["profile"] not in dict_conf.keys():
            raise Http404
        return super(ProfileDetailUpdate, self).dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        return eval(
            dict_conf[self.kwargs["profile"]][0]
        )

    def get_object(self):
        obj = get_object_or_404(
            eval(
                f"{dict_conf[self.kwargs['profile']][1]}.objects.defer('user')"
            ),
            slug=self.kwargs["slug"]
        )
        if not self.request.user.is_staff and obj.user != self.request.user:
            raise Http404
        return obj

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions

from django.shortcuts import get_object_or_404
from django.http import Http404
from .serializers import (
    ProfileSerializer,
    AboutMeSerializer,
    PersonalInformationSerializer,
    WorkExperienceSerializer,
    EducationalRecordSerializer
)

from bucket import bucket
from permissions import IsStaffOrOwner, IsSuperUserOrReadOnly
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
    permission_classes = (IsStaffOrOwner,)
    lookup_field = "slug"

    def dispatch(self, request, *args, **kwargs):
        if self.kwargs["profile"] not in dict_conf.keys():
            raise Http404
        return super(ProfileDetailUpdate, self).dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        return eval(
            dict_conf[self.kwargs['profile']][0]
        )

    def get_object(self):
        obj = get_object_or_404(
            eval(
                f"{dict_conf[self.kwargs['profile']][1]}.objects.defer('user')"
            ),
            slug=self.kwargs["slug"]
        )
        return obj

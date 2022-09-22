from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import exceptions

from .serializers import ProfileSerializer, AboutMeSerializer
from accounts.models.profiles import (
    Profile,
    AboutMe,
    WorkExperience,
    PersonalInformation,
    EducationalRecord
)


class ProfileDetailUpdate(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializers = (
            "ProfileSerializer",
            "PersonalInformationSerializer",
            "AboutMeSerializer",
            "WorkExperienceSerializer",
            "EducationalRecordSerializer"
        )
        models = (
            "Profile",
            "AboutMe",
            "WorkExperience",
            "PersonalInformation",
            "EducationalRecord"
        )
        lookups = ("p", "pi", "am", "we", "er")

        if (get_lookup := self.kwargs["profile"]) not in lookups:
            raise exceptions.NotFound

        self.queryset = eval()
        self.serializer_class = eval(serializers[lookups.index(get_lookup)])
        return super(ProfileDetailUpdate, self).get_serializer(*args, **kwargs)

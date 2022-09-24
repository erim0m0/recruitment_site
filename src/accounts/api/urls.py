from django.urls import path

from .profiles_views import ProfileDetailUpdate
from .authentication_views import (
    Register, Login, VerifyOtp,
)

urlpatterns = [
    path("sign-up/", Register.as_view(), name="register"),
    path("sign-in/", Login.as_view(), name="login"),
    path("verify/", VerifyOtp.as_view(), name="verify"),
    path("detail/<str:profile>/<slug:slug>/", ProfileDetailUpdate.as_view(), name="profile"),
]

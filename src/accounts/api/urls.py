from django.urls import path

from .profiles_views import ProfileDetailUpdate
from .authentication_views import (
    Register, Login, VerifyOtp,
    UsersList,
)

urlpatterns = [
    path("sign-up/", Register.as_view(), name="register"),
    path("sign-in/", Login.as_view(), name="login"),
    path("verify/", VerifyOtp.as_view(), name="verify"),
    path("users/", UsersList.as_view(), name="users"),
    path("profile/<str:profile>/<int:pk>/", ProfileDetailUpdate.as_view(), name="profile"),
    path("profile/about-me/<int:pk>/", ProfileDetailUpdate.as_view(), name="profile"),
    path("profile/about-me/<int:pk>/", ProfileDetailUpdate.as_view(), name="about_me"),
]

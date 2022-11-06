from django.urls import path

from .profiles_views import ProfileDetailUpdate
from .authentication_views import (
    Register, Login,
    VerifyOtp, DeleteAccount
)
from .company_interface import (
    CompanyProfileView,
    CompanyProfileCreateView,
)

app_name = "api"

urlpatterns = [
    # Authentication
    path("sign-up/", Register.as_view(), name="register"),
    path("operator/sign-up/", Register.as_view(), name="operator-register"),
    path("sign-in/", Login.as_view(), name="login"),
    path("operator/sign-in/", Login.as_view(), name="operator-login"),
    path("verify/", VerifyOtp.as_view(), name="verify"),
    path("operator/verify/", VerifyOtp.as_view(), name="operator-verify"),
    path("delete-account/", DeleteAccount.as_view(), name="delete-account"),
    # User's Profile
    path("profile/<slug:slug>/", ProfileDetailUpdate.as_view(), name="profile"),
    path("profile/<str:profile>/<slug:slug>/", ProfileDetailUpdate.as_view(), name="work-experience"),
    path("profile/<str:profile>/<slug:slug>/", ProfileDetailUpdate.as_view(), name="educational-record"),
    path("profile/<str:profile>/<slug:slug>/", ProfileDetailUpdate.as_view(), name="cv"),
    # Company's Profile
    path("company/profile/", CompanyProfileCreateView.as_view(), name="company-profile-create"),
    path("company/profile/<int:pk>/", CompanyProfileView.as_view(), name="company-profile"),
    # TODO: Add url for authentication for operator company
]

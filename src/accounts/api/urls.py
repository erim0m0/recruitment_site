from django.urls import path

from .profiles_views import ProfileDetailUpdate
from .authentication_views import (
    Register, Login, VerifyOtp, DeleteAccount
)
from .company_interface import (
    CompanyProfileRetrieveUpdateDestroy,
    OperatorProfile,
)

app_name = "api"

urlpatterns = [
    path("sign-up/", Register.as_view(), name="register"),
    path("operator/sign-up/", Register.as_view(), name="operator-register"),
    path("sign-in/", Login.as_view(), name="login"),
    path("verify/", VerifyOtp.as_view(), name="verify"),
    path("operator/verify/", VerifyOtp.as_view(), name="operator-verify"),
    path("delete-account/", DeleteAccount.as_view(), name="delete-account"),
    path("detail/<str:profile>/<slug:slug>/", ProfileDetailUpdate.as_view(), name="profile"),
    path("operator-profile/<slug:slug>/", OperatorProfile.as_view(), name="operator-register"),
    path("company-profile/<int:pk>/", CompanyProfileRetrieveUpdateDestroy.as_view(), name="company-profile"),
    # TODO: Add url for authentication for operator company
]

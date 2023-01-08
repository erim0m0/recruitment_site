from django.urls import path

from .user_profile import ProfileView, WorkExperienceView, EducationalRecordView
from .authentication import (
    ChangeTwoStepPassword, VerifyOtp, Register, DeleteAccount,CreateTwoStepPassword,
    Login, VerifyTwoStepPassword,
)
from .company import (
    CompanyProfileDetailDestroy, CompaniesList, CompanyProfileCreate, CompanyProfileUpdate
)

app_name = "api"

urlpatterns = [
    # AUTHENTICATION
    path("sign-up/", Register.as_view(), name="register"),
    path("operator/sign-up/", Register.as_view(), name="operator-register"),
    path("sign-in/", Login.as_view(), name="login"),
    path("operator/sign-in/", Login.as_view(), name="operator-login"),
    path("verify/", VerifyOtp.as_view(), name="verify"),
    path("operator/verify/", VerifyOtp.as_view(), name="operator-verify"),
    path("delete-account/", DeleteAccount.as_view(), name="delete-account"),
    path("verify-two-step-password/", VerifyTwoStepPassword.as_view(), name="verify-two-step-password"),
    path("change-two-step-password/", ChangeTwoStepPassword.as_view(), name="change-two-step-password"),
    path("create-two-step-password/", CreateTwoStepPassword.as_view(), name="create-two-step-password"),
    # USER'S PROFILE
    path("profile/<slug:slug>/", ProfileView.as_view(), name="profile"),
    path("profile/work-exp/<slug:slug>/", WorkExperienceView.as_view(), name="work-experience"),
    path("profile/ed-record/<slug:slug>/", EducationalRecordView.as_view(), name="educational-record"),
    # COMPANY'S PROFILE
    path("companies/", CompaniesList.as_view(), name="companies-list"),
    path("company/profile/", CompanyProfileCreate.as_view(), name="company-profile-create"),
    path("company/profile/<int:pk>/", CompanyProfileDetailDestroy.as_view(), name="company-profile-detail"),
    path("company/profile/update/<int:pk>/", CompanyProfileUpdate.as_view(), name="company-profile-update"),
]

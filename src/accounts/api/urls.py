from django.urls import path

from accounts.api import user_profile, authentication, company

app_name = "api"

urlpatterns = [
    # AUTHENTICATION
    path("sign-up/", authentication.Register.as_view(), name="register"),
    path("operator/sign-up/", authentication.Register.as_view(), name="operator-register"),
    path("sign-in/", authentication.Login.as_view(), name="login"),
    path("operator/sign-in/", authentication.Login.as_view(), name="operator-login"),
    path("verify/", authentication.VerifyOtp.as_view(), name="verify"),
    path("operator/verify/", authentication.VerifyOtp.as_view(), name="operator-verify"),
    path("delete-account/", authentication.DeleteAccount.as_view(), name="delete-account"),
    path("verify-two-step-password/", authentication.VerifyTwoStepPassword.as_view(), name="verify-two-step-password"),
    path("change-two-step-password/", authentication.ChangeTwoStepPassword.as_view(), name="change-two-step-password"),
    path("create-two-step-password/", authentication.CreateTwoStepPassword.as_view(), name="create-two-step-password"),
    # USER'S PROFILE
    path("profile/", user_profile.CreateProfile.as_view(), name="create-profile"),
    path("profile/work-exp/", user_profile.CreateWorkExperience.as_view(), name="create-work-experience"),
    path("profile/ed-record/", user_profile.CreateEducationalRecord.as_view(), name="create-educational-record"),
    path("profile/<str:phone>/", user_profile.ProfileView.as_view(), name="profile"),
    path("profile/work-exp/<int:pk>/", user_profile.WorkExperienceView.as_view(), name="work-experience"),
    path("profile/ed-record/<int:pk>/", user_profile.EducationalRecordView.as_view(), name="educational-record"),
    # COMPANY'S PROFILE
    path("companies/", company.CompaniesList.as_view(), name="companies-list"),
    path("company/profile/", company.CompanyProfileCreate.as_view(), name="company-profile-create"),
    path("company/profile/<int:pk>/", company.CompanyProfileDetailDestroy.as_view(), name="company-profile-detail"),
    path("company/profile/update/<int:pk>/", company.CompanyProfileUpdate.as_view(), name="company-profile-update"),
]

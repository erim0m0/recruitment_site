from django.urls import path

from .views import (
    Register, Login, VerifyOtp,
    UsersList,
)

urlpatterns = [
    path("sign-up/", Register.as_view(), name="register"),
    path("sign-in/", Login.as_view(), name="login"),
    path("verify/", VerifyOtp.as_view(), name="verify"),
    path("users/", UsersList.as_view(), name="users"),
]

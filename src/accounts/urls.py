from django.urls import path
from .views import SignUpView, OTPCheckView

urlpatterns = [
    path('', SignUpView.as_view(), name='signUp-In'),
    path('otp-check/', OTPCheckView.as_view(), name='OTP_check'),
]

from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import SignUpView, OTPCheckView, send_otp_code_again, SignInView, Register

urlpatterns = [
    path('api/', include('accounts.api.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('sign-up/', Register.as_view(), name='signUp'),
    path('sign-in/', SignInView.as_view(), name='signIn'),
    path('otp-check/', OTPCheckView.as_view(), name='OTP_check'),
    path('send-otpcode-again/', send_otp_code_again, name='send_OTPcode_again'),
]

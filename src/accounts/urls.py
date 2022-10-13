from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name = "account"

urlpatterns = [
    path('api/', include('accounts.api.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

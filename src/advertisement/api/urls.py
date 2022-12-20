from django.urls import path

from advertisement.api.views import (
    AdertisementsList, AdvertisementDetail,
    AdvertisementCreateView
)

urlpatterns = [
    path('list/', AdertisementsList.as_view(), name="advertisements-list"),
    path('', AdvertisementCreateView.as_view(), name="create-advertisement"),
    path('<int:pk>/', AdvertisementDetail.as_view(), name="advertisement"),
]

from rest_framework import routers

from django.urls import path

from advertisement.api.views import (
    AdertisementsList,
    AdvertisementView,
    AdvertisementCreateView
)

urlpatterns = [
    path('list/', AdertisementsList.as_view(), name="advertisements-list"),
    path('', AdvertisementCreateView.as_view(), name="create-advertisement"),
    path('<int:pk>/', AdvertisementView.as_view(), name="advertisement"),
]

# router = routers.SimpleRouter()
# router.register('advertisement', AdertisementsList, basename="advertisement")
# urlpatterns = router.urls

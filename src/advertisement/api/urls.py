from rest_framework import routers

from django.urls import path

from advertisement.api.views import AdertisementsList, AdvertisementAPIView

urlpatterns = [
    path('list/', AdertisementsList.as_view(), name="advertisements-list"),
    path('<int:pk>/', AdvertisementAPIView.as_view(), name="advertisement"),
]

# router = routers.SimpleRouter()
# router.register('advertisement', AdertisementsList, basename="advertisement")
# urlpatterns = router.urls

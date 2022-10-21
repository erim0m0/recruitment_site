from rest_framework import routers

from django.urls import path

from advertisement.api.views import AvertisementApiView


router = routers.SimpleRouter()
router.register('advertisement', AvertisementApiView, basename="advertisement")
urlpatterns = router.urls

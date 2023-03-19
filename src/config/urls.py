from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="IRANABLE API",
        default_version='v1.0.0',
        description="API's Iranable",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="iranable.aj.am@gmail.com"),
        license=openapi.License(name="IAM License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='account')),
    path('advertisement/', include('advertisement.urls', namespace='advertisement')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# add root static files
urlpatterns = urlpatterns + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

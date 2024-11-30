from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
import rest_framework
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


docpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/expense/', include('expense.urls')),
] + docpatterns
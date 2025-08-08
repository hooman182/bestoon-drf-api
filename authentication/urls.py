from django.urls import include, path
import authentication.spectacular_extensions

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include("djoser.urls.jwt")),
]
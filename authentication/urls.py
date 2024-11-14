from django.urls import path

from authentication.views import UserLoginView, UserLogoutView, UserRegisterationView


urlpatterns = [
    path('users/create', UserRegisterationView.as_view(), name='user-register'),
    path('users/login', UserLoginView.as_view(), name='user-login'),
    path('users/logout', UserLogoutView.as_view(), name='user-login'),
]

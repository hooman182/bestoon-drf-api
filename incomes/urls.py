from django.urls import path
from .views import IncomeListViews


urlpatterns = [
    path('incomes/', IncomeListViews.as_view(), name='incomes-list')
]
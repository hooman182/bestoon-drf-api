from django.urls import path
from .views import IncomeListCreateView, IncomeRetrieveView


urlpatterns = [
    path('', IncomeListCreateView.as_view(), name='incomes-list'),
    path('', IncomeRetrieveView.as_view(), name='incomes-create'),
]
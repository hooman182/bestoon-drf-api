from django.urls import path
from .views import IncomeListViews, IncomeCreateView


urlpatterns = [
    path('', IncomeListViews.as_view(), name='incomes-list'),
    path('', IncomeCreateView.as_view(), name='incomes-create'),
]
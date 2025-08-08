from django.urls import path

from .views import IncomeListCreateView, IncomeRetrieveView

urlpatterns = [
    path("", IncomeListCreateView.as_view(), name="incomes"),
    path("<pk>", IncomeRetrieveView.as_view(), name="incomes-retrieve"),
]

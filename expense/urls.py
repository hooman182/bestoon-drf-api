from rest_framework.routers import DefaultRouter
from expense.views import ExpenseViewSet


router = DefaultRouter()
router.register('expenses', ExpenseViewSet, 'expenses')

urlpatterns = router.urls

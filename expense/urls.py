from rest_framework.routers import DefaultRouter

from expense.views import ExpenseViewSet

router = DefaultRouter()
router.register('', ExpenseViewSet, 'expenses')

urlpatterns = router.urls

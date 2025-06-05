from rest_framework.routers import DefaultRouter
from expense.views import CategoryViewSet, ExpenseViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, 'categories')
router.register('expenses', ExpenseViewSet, 'expenses')

urlpatterns = router.urls

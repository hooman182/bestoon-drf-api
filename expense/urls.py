from rest_framework.routers import DefaultRouter
from expense.views import CategoryViewSet, CollectionView, ExpenseViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, 'categories')
router.register('collections', CollectionView, 'collections')
router.register('expenses', ExpenseViewSet, 'expenses')

urlpatterns = router.urls

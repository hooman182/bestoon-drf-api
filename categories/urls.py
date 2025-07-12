from rest_framework.routers import DefaultRouter
from expense.views import CategoryViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, 'categories')

urlpatterns = router.urls

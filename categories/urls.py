from rest_framework.routers import DefaultRouter
from .views import CategoryViewSets


router = DefaultRouter()
router.register('categories', CategoryViewSets, 'categories')

urlpatterns = router.urls

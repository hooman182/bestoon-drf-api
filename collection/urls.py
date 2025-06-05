from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet


router = DefaultRouter()
router.register('collections', CollectionViewSet, 'collections')

urlpatterns = router.urls
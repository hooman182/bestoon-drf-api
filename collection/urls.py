from rest_framework.routers import DefaultRouter

from .views import CollectionViewSet

router = DefaultRouter()
router.register('', CollectionViewSet, 'collections')

urlpatterns = router.urls
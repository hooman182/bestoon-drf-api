from rest_framework import viewsets, permissions

from collection.models import Collection
from collection.serializers import CollectionSerializer
from .permissions import OwnerPermission
#---------------------------------------------------------------


class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, OwnerPermission]
    serializer_class = CollectionSerializer

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise ValueError("User is not authenticated")
        
        serializer.save(user=self.request.user)
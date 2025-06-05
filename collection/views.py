from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from collection.models import Collection
from collection.serializers import CollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
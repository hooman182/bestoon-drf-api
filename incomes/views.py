from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from collection.models import Collection

from .models import Income
from .serializers import IncomesSerilizer

# ------------------------------------------------------------------------


class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomesSerilizer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["collections_queryset"] = Collection.objects.filter(
            user=self.request.user
        )
        return context


class IncomeRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomesSerilizer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["collections_queryset"] = Collection.objects.filter(
            user=self.request.user
        )
        return context

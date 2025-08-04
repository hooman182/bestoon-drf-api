from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from expense.models import Expense
from expense.serializers import ExpenseSerializer

# ------------------------------------------------------------------------


class ExpenseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise ValueError("User is not authenticated")

        serializer.save(user=self.request.user)

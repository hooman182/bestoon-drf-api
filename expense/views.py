from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from expense.models import Expense
from expense.serializers import ExpenseSerializer
#------------------------------------------------------------------------


class ExpenseViewSet(viewsets.ViewSet):

    permission_classes = []
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    def list(self, request):
        serializer = ExpenseSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        expense = get_object_or_404(Expense, pk=pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def create(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'expense created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        serializer = ExpenseSerializer(data=request.data)
        expense = Expense.objects.get(pk=pk)
        return Response({'msg': 'record updated'}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        expense = Expense.objects.get(pk=pk)
        expense.delete()
        return Response({'msg': 'record deleted'}, status=status.HTTP_200_OK)
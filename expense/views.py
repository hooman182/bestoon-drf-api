from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from expense.models import Category, Collection, Expense
from expense.serializers import CategorySerializer, CollectionSerializer, ExpenseSerializer


class ExpenseViewSet(viewsets.ViewSet):

    permission_classes = []
    queryset = Expense.objects.all()

    def list(self, request):
        serializer = ExpenseSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        expense = get_object_or_404(Expense, pk=pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'expense created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        serializer = ExpenseSerializer(data=request.data)
        expense = Expense.objects.get(pk=pk)

    def destroy(self, request, pk=None):
        expense = Expense.objects.get(pk=pk)
        expense.delete()
        return Response({'msg': 'record deleted'}, status=status.HTTP_200_OK)


class CollectionView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
  
    
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
  

# class CategoryViewSet(viewsets.ViewSet):

#     permission_classes = [IsAuthenticated]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def list(self, request):
#         serializer = CategorySerializer(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         category = get_object_or_404(Category, pk=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'category created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

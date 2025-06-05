from rest_framework import serializers

from expense.models import Category, Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = '__all__'
        
        
class CategorySerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(max_length=200)
    
    class Meta:
        model = Category
        fields = ('name',)
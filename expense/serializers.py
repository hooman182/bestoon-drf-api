from rest_framework import serializers

from expense.models import Category, Collection, Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = '__all__'
        
        
class CollectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Collection
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(max_length=200)
    
    class Meta:
        model = Category
        fields = ('name',)
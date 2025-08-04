from rest_framework import serializers

from collection.models import Collection
from expense.models import Expense

# -----------------------------------------------


class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ("user",)

    def validate_collection(self, value):
        user = self.context["request"].user

        if value.user != user:
            raise serializers.ValidationError("collection selected is wrong")

        return value
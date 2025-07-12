from rest_framework import serializers
from .models import Income

class IncomesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
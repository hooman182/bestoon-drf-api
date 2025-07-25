from rest_framework import serializers
from .models import Collection
#-----------------------------------------
   
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection 
        fields = ('title', 'description', 'currency', 'id')
        read_only_fields = ('user',)
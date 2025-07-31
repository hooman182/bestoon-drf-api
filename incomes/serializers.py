from rest_framework import serializers
from .models import Income
from collection.models import Collection
#-----------------------------------------------------

class IncomesSerilizer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    class Meta:
        model = Income
        fields = "__all__"
        read_only_fields = ["user"]

    def get_collection(self, obj):
        return obj.collection_id

    def validate_collection(self, value):
        user = self.context["request"].user

        if value.user != user:
            raise serializers.ValidationError("You are selected wrong collection")

        return value

    def validate(self, data):
        if not self.context["request"].user.is_authenticated:
            raise serializers.ValidationError("You are not authenticated")

        data["user"] = self.context["request"].user
        return data

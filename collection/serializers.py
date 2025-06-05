from email.policy import default
from rest_framework import serializers


class CollectionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=120)
    currency = serializers.ChoiceField(
        choices=[("IRT", "تومان"), ("IRR", "ریال"), ("USD", "دلار")], default="IRT"
    )

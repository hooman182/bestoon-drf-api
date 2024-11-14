from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'},)

    class Meta:
        model = User
        fields = ('email', 'password',)

    def create(self, validated_data):
        print(validated_data)
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
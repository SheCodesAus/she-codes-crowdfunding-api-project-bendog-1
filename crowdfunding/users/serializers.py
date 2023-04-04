from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class CustomUserDetailSerializer(serializers.ModelSerializer):
    """ a detail serializer for our user class """
    
    class Meta:
        model = CustomUser
        exclude = [
            'password', 
            'is_superuser', 
            'is_staff', 
            'is_active', 
            'groups', 
            'user_permissions',
        ]


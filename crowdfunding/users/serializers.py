from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

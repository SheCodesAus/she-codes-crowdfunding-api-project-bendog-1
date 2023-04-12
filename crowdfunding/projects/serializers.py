from rest_framework import serializers

from .models import Project, Pledge


class PledgeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pledge 
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'goal', 'image', 'is_open', 'date_created', 'owner']


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)


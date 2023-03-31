from rest_framework import serializers

from .models import Mentor, Event, Onboarding


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name', 'mentors']
        read_only_fields = ['id',]

# class OnboardingStatusSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = OnboardingStatus
#         fields = "__all__"
#         read_only_fields = ['id', 'added_at', 'added_by']

# class OnboardingStatusSmallSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = OnboardingStatus
#         fields = ['stage', 'complete']
#         read_only_fields = ['id', 'added_at', 'added_by']


class OnboardingSerializer(serializers.ModelSerializer):
    # statuses = OnboardingStatusSmallSerializer(many=True)
    event = EventSerializer(read_only=True)
    class Meta:
        model = Onboarding
        fields = "__all__"
        read_only_fields = ['id',]

class MentorSerializer(serializers.ModelSerializer):
    events = OnboardingSerializer(many=True, source="onboardings")
    class Meta:
        model = Mentor
        fields = ['id', 'name', 'events']
        read_only_fields = ['id',]
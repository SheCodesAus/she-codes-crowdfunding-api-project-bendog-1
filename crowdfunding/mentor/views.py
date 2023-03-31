from django.shortcuts import render
from rest_framework import generics

from .serializers import MentorSerializer, EventSerializer, OnboardingSerializer
from .models import Mentor, Event, Onboarding

# Create your views here.

class MentorListView(generics.ListCreateAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()

class EventListView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class OnboardingListView(generics.ListCreateAPIView):
    serializer_class = OnboardingSerializer
    queryset = Onboarding.objects.all()

class OnboardingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OnboardingSerializer
    queryset = Onboarding.objects.all()



# class OnboardingStatusListView(generics.ListCreateAPIView):
#     serializer_class = OnboardingStatusSerializer
#     queryset = OnboardingStatus.objects.all()
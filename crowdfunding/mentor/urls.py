from django.urls import path

from . import views

urlpatterns = [
    path('mentor/', views.MentorListView.as_view(), name="mentor-list"),
    path('event/', views.EventListView.as_view(), name="event-list"),
    path('onboarding/', views.OnboardingListView.as_view(), name="onboarding-list"),
    path('onboarding/<int:pk>/', views.OnboardingDetailView.as_view(), name="onboarding-detail"),
    # path('status/', views.OnboardingStatusListView.as_view(), name="onboardingstatus-list"),

]

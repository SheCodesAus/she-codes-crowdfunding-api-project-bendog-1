from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class Mentor(models.Model):

    name = models.CharField(max_length=60)    

    class Meta:
        verbose_name = "mentor"
        verbose_name_plural = "mentors"

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=60)
    date = models.DateField()   

    mentors = models.ManyToManyField(Mentor, related_name="events", through="mentor.Onboarding")

    def __str__(self):
        return self.name

class Onboarding(models.Model):

    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='onboardings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    interview_done = models.BooleanField()
    offer_done = models.BooleanField()
    contract_done = models.BooleanField()

    def __str__(self):
        return f"{self.event}::{self.mentor}"


# class OnboardingStatus(models.Model):
#     STAGES = (
#         ("INTERVIEW", "Interview"),
#         ("OFFER", "Offer"),
#     )

#     onboarding = models.ForeignKey(Onboarding, related_name="statuses", on_delete=models.CASCADE)
#     added_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     added_at = models.DateTimeField(auto_now_add=True)
#     stage = models.CharField(max_length=32, choices=STAGES)
#     complete = models.BooleanField(default=None, null=True, blank=True)

#     class Meta:
#         unique_together = ['stage', 'onboarding']
    

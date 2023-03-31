# Generated by Django 4.1.5 on 2023-03-31 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Mentor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
            ],
            options={
                "verbose_name": "mentor",
                "verbose_name_plural": "mentors",
            },
        ),
        migrations.CreateModel(
            name="Onboarding",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mentor.event"
                    ),
                ),
                (
                    "mentor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mentor.mentor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OnboardingStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                (
                    "stage",
                    models.CharField(
                        choices=[("INTERVIEW", "Interview"), ("OFFER", "Offer")],
                        max_length=32,
                    ),
                ),
                ("complete", models.BooleanField(blank=True, default=None, null=True)),
                (
                    "added_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "onboarding",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statuses",
                        to="mentor.onboarding",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="mentors",
            field=models.ManyToManyField(
                related_name="events", through="mentor.Onboarding", to="mentor.mentor"
            ),
        ),
    ]
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.forms import ModelForm

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token_balance = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.token_balance}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class JobField(models.Model):
    ART = "A"
    BUSINESS = "B"
    COMPUTERS = "C"
    EDUCATION = "ED"
    ENGINEERING = "ENG"
    FINANCE = "F"
    LAW = "L"
    LITERATURE = "LIT"
    MEDICINE = "M"
    SCIENCE = "SC"
    SOCIALSCI = "SS"
    TECHNOLOGY = "TECH"

    JOB_CHOICES = [
        (ART, "Art"),
        (BUSINESS, "Business"),
        (COMPUTERS, "Computers"),
        (EDUCATION, "Education"),
        (ENGINEERING, "Engineering"),
        (FINANCE, "Finance"),
        (LAW, "Law"),
        (LITERATURE, "Literature"),
        (MEDICINE, "Medicine"),
        (SCIENCE, "Science"),
        (SOCIALSCI, "Social Sciences"),
        (TECHNOLOGY, "Technology"),
    ]


class Job(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=False)
    description = models.TextField(blank=False)
    source_language = models.TextField(blank=False)
    target_language = models.TextField(blank=False)
    job_field = models.CharField(
        max_length=4,
        choices=JobField.JOB_CHOICES,
        default=JobField.LITERATURE,
    )
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    text = models.TextField(blank=False)

    def __str__(self):
        return f"{self.id}-{self.title[:30]}-{self.description[:100]}-{self.source_language[:15]}-{self.target_language[:15]}-{self.job_field}-{self.budget}-{self.text}"

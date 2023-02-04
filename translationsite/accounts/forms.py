from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, Select
from app.models import UserProfile


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


CHOICES = ((True, "Yes"), (False, "No"))


class UserProfileSignupForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["is_translator"]
        widgets = {"is_translator": CheckboxInput(attrs={"class": "checkbox-inline"})}

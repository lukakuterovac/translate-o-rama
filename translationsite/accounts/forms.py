from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, Select
from app.models import UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data


CHOICES = ((True, "Yes"), (False, "No"))


class UserProfileSignupForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["is_translator"]
        widgets = {"is_translator": CheckboxInput(attrs={"class": "checkbox-inline"})}


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "password"]

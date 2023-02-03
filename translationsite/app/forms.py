from django.forms import ModelForm
from .models import Job, JobBid, Message, UserProfile
from django.contrib.auth.forms import SetPasswordForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class UserProfileForm(ModelForm):
    is_translator = forms.BooleanField()

    class Meta:
        model = UserProfile
        fields = [
            "token_balance",
            "is_translator",
        ]

        widgets = {
            "token_balance": forms.NumberInput(attrs={"class": "form-control"}),
            "is_translator": forms.CheckboxInput(attrs={"class": "form-control"}),
        }


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "description",
            "source_language",
            "target_language",
            "job_field",
            "budget",
            "text",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "source_language": forms.TextInput(attrs={"class": "form-control"}),
            "target_language": forms.TextInput(attrs={"class": "form-control"}),
            "job_field": forms.Select(attrs={"class": "form-control"}),
            "budget": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean(self):
        errors = []
        if (
            "source_language" in self.cleaned_data
            and "target_language" in self.cleaned_data
        ):
            if (
                self.cleaned_data["source_language"].lower()
                == self.cleaned_data["target_language"].lower()
            ):
                errors.append(
                    ValidationError("Source and target language must be different!")
                )
        else:
            errors.append(ValidationError("Language fields empty"))

        if "budget" in self.cleaned_data:
            if self.cleaned_data["budget"] <= 0:
                errors.append(ValidationError("Budget must be greater than 0!"))
        else:
            errors.append(ValidationError("Budget field empty"))

        if "title" in self.cleaned_data:
            if Job.objects.filter(title=self.cleaned_data["title"]):
                errors.append(ValidationError("A job with this title already exists."))

        else:
            errors.append(ValidationError("Title fields empty"))

        if errors:
            raise ValidationError(errors)
        return self.cleaned_data


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ["new_password1", "new_password2"]


class EmailChangeForm(forms.Form):
    """
    A form that lets a user change set their email while checking for a change in the
    e-mail.
    """

    error_messages = {
        "email_mismatch": ("The two email addresses fields didn't match."),
        "not_changed": ("The email address is the same as the one already defined."),
    }

    new_email1 = forms.EmailField(
        label=("New email address"),
        widget=forms.EmailInput,
    )

    new_email2 = forms.EmailField(
        label=("New email address confirmation"),
        widget=forms.EmailInput,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get("new_email1")
        if new_email1 and old_email:
            if new_email1 == old_email:
                raise forms.ValidationError(
                    self.error_messages["not_changed"],
                    code="not_changed",
                )
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get("new_email1")
        new_email2 = self.cleaned_data.get("new_email2")
        if new_email1 and new_email2:
            if new_email1 != new_email2:
                raise forms.ValidationError(
                    self.error_messages["email_mismatch"],
                    code="email_mismatch",
                )
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user


class JobBidForm(ModelForm):
    class Meta:
        model = JobBid
        fields = ["bid"]
        widgets = {
            "bid": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "0.0"}
            ),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(JobBidForm, self).__init__(*args, **kwargs)

    def clean(self):
        if "bid" in self.cleaned_data:
            if self.cleaned_data["bid"] > self.user.userprofile.token_balance:
                raise ValidationError("User doesn't have enough tokens!")
        return self.cleaned_data


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            "text",
        ]


class CompleteJobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            "translation",
        ]

    def clean(self):
        if "translation" in self.cleaned_data:
            if self.cleaned_data["translation"] == "":
                raise ValidationError("You have to translate text!")
        return self.cleaned_data

    def save(self, commit=True):
        translation = self.cleaned_data["translation"]
        self.instance.translation = translation
        if commit:
            self.instance.save()
        return self.instance

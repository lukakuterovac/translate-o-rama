from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Job, UserProfile
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

            if Job.objects.get(title=self.cleaned_data["title"]):

                errors.append(ValidationError("A job with this title already exists."))

        else:
            errors.append(ValidationError("Title fields empty"))

        if errors:
            raise ValidationError(errors)
        return self.cleaned_data

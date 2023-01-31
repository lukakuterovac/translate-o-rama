from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Job


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
        if errors:
            raise ValidationError(errors)
        return self.cleaned_data

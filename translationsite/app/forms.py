from django.forms import ModelForm
from .models import Job
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model


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


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ["new_password1", "new_password2"]

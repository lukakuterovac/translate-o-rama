from django import forms
from django.contrib.auth.models import User
from .models import JobField, Job


class JobForm(forms.Form):
    user = forms.ForeignKey(User, on_delete=forms.CASCADE)
    title = forms.TextField(blank=False)
    description = forms.TextField(blank=False)
    source_language = forms.TextField(blank=False)
    target_language = forms.TextField(blank=False)
    job_field = forms.ModelChoiceField(
        queryset=Job.objects.values_list("job_field", flat=True),
        label="Job field:",
    )
    budget = forms.DecimalField(max_digits=10, decimal_places=2)
    text = forms.TextField(blank=False)

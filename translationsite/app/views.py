from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Job
from .forms import JobForm


def home(request):
    context = {}
    return render(request, "app/home.html", context)


def dashboard(request):
    user = request.user
    jobs = Job.objects.filter(user=user)
    context = {
        "user": user,
        "jobs": jobs,
    }
    return render(request, "app/dashboard.html", context)


def post_job(request):

    form = JobForm(initial={"job_field": "ART"})
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job_post = Job.objects.create(
                user=request.user,
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                source_language=form.cleaned_data.get("source_language"),
                target_language=form.cleaned_data.get("target_language"),
                job_field=form.cleaned_data.get("job_field"),
                budget=form.cleaned_data.get("budget"),
                text=form.cleaned_data.get("text"),
            )
            return HttpResponseRedirect(reverse("app:post_job", args=[]))
        else:
            errors = []
            for k, v in form.errors.items():
                errors.append(v)
            return render(
                request, "app/post_job.html", {"form": form, "errors": errors}
            )
    else:
        form = JobForm()
    return render(request, "app/post_job.html", {"form": form})

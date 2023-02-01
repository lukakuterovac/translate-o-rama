from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Job, Message
from .forms import JobForm
from django.contrib.auth.models import User


def home(request):
    context = {}
    return render(request, "app/home.html", context)


def dashboard(request):
    user = request.user
    jobs = Job.objects.filter(user=user)
    messages = Message.objects.filter(to_user=user).order_by("send_date").reverse()
    context = {
        "user": user,
        "jobs": jobs,
        "messages": messages,
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

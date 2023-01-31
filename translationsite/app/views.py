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
    context = {
        "user": user,
    }
    return render(request, "app/dashboard.html", context)


def post_job(request):
    if request.method == "POST":
        job_post = Job.objects.create(
            user=request.user,
            title=request.POST["title"],
            description=request.POST["description"],
            source_language=request.POST["source_language"],
            target_language=request.POST["target_language"],
            job_field=request.POST["job_field"],
            budget=request.POST["budget"],
            text=request.POST["text"],
        )
        return HttpResponseRedirect(reverse("app:post_job", args=[]))
    context = {"form": JobForm()}
    return render(request, "app/post_job.html", context)

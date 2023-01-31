from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Job


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
            source_language=request.POST["source_lang"],
            target_language=request.POST["target_lang"],
            job_field=request.POST["job_field"],
            budget=request.POST["budget"],
            text=request.POST["text"],
        )
        return HttpResponseRedirect(reverse("app:post_job", args=[]))
    return render(request, "app/post_job.html", {})

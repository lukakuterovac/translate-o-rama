from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Job
from .forms import JobForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SetPasswordForm
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    return render(request, "app/home.html", context)


def dashboard(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "app/dashboard.html", context)


def profile(request):
    user = request.user
    form = SetPasswordForm(user)
    context = {"user": user, "form": form}
    return render(request, "app/profile.html", context)


def change_email(request):
    if request.method == "POST":
        user = request.user
        email = request.POST["email"]
        user.email = email
        return HttpResponseRedirect(reverse("app:profile", args=[]))
    return render(request, "app/profile.html", {})


def change_password(request):
    user = request.user
    if request.method == "POST":
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect("login")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        context = {"user": user, "form": form}
        return HttpResponseRedirect(request, "app/profile.html", context)
    else:
        form = SetPasswordForm(user)
        context = {"user": user, "form": form}
        return render(request, "app/profile.html", context)


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

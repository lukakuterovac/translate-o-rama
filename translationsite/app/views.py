from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Job
from .forms import JobForm, EmailChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


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
    email_form = EmailChangeForm(user)
    password_form = SetPasswordForm(user)
    context = {
        "user": user,
        "email_form": email_form,
        "password_form": password_form,
    }
    return render(request, "app/profile.html", context)


@login_required()
def email_change(request):
    user = request.user
    form = EmailChangeForm(user)

    if request.method == "POST":
        form = EmailChangeForm(user, request.POST)
        password_form = SetPasswordForm(user)

        if form.is_valid():
            form.save()
            context = {
                "user": user,
                "email_form": form,
                "password_form": password_form,
            }

            return HttpResponseRedirect(reverse("app:profile", args=[]))
        else:
            context = {"user": user, "email_form": form, "password_form": password_form}
            return render(request, "app/profile.html", context)
    else:

        return render(
            request,
            "app/profile.html",
            {"email_form": form},
            context_instance=RequestContext(request),
        )


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

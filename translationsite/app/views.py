from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import JobForm, EmailChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Job, Message
from .forms import JobForm
from django.db.models import Q


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


def jobs(request):
    user = request.user
    jobs = Job.objects.all().filter(~Q(user=user), Q(is_assigned=False))

    context = {
        "user": user,
        "jobs": jobs,
    }
    return render(request, "app/jobs.html", context)


def job_bid(request):
    user = request.user
    jobs = Job.objects.all().filter(~Q(user=user), Q(is_assigned=False))
    context = {
        "user": user,
        "jobs": jobs,
    }
    return HttpResponseRedirect(request, "app/jobs.html", context)


def job_message(request):
    pass

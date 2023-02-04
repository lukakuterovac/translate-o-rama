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
from .models import Job, Message, JobBid, UserProfile, JobField
from .forms import JobForm, MessageForm, JobBidForm, DisputeJobForm
from django.db.models import Q
from django.contrib.auth.models import User


def home(request):
    user = request.user
    translators = UserProfile.objects.filter(Q(is_translator=True))
    available_jobs = Job.objects.filter(Q(is_assigned=False), Q(is_completed=False))
    job_fields = JobField.objects.all()

    job_field_query = request.GET.get("job_field")
    target_language_query = request.GET.get("target_language")
    source_language_query = request.GET.get("target_language")

    if (
        target_language_query != ""
        and target_language_query is not None
        and job_field_query != ""
        and job_field_query is not None
    ):
        available_jobs = available_jobs.filter(
            Q(job_field__icontains=job_field_query),
            Q(target_language__icontains=target_language_query)
            | Q(source_language__icontains=source_language_query),
        ).distinct()

    elif target_language_query != "" and target_language_query is not None:
        available_jobs = available_jobs.filter(
            Q(target_language__icontains=target_language_query)
            | Q(source_language__icontains=source_language_query)
        )
    elif job_field_query != "" and job_field_query is not None:
        available_jobs = available_jobs.filter(job_field__icontains=job_field_query)

    context = {
        "translators": translators,
        "available_jobs": available_jobs,
        "user": user,
        "job_fields": job_fields,
    }

    return render(request, "app/home.html", context)


def dashboard(request):
    user = request.user
    jobs = Job.objects.filter(user=user)
    messages = Message.objects.filter(to_user=user).order_by("send_date").reverse()
    bids = []
    temp = JobBid.objects.all()
    for job in jobs:
        for bid in temp:
            if bid.job == job:
                bids.append(bid)

    translators_bid = JobBid.objects.filter(Q(bid_user=user))
    assigned_jobs = Job.objects.filter(
        Q(translator=user), Q(is_assigned=True)
    )  # jobs that are not from user
    completed_jobs = Job.objects.filter(Q(translator=user), Q(is_completed=True))

    context = {
        "user": user,
        "jobs": jobs,
        "messages": messages,
        "bids": bids,
        "translator_bids": translators_bid,
        "assigned_jobs": assigned_jobs,
        "completed_jobs": completed_jobs,
    }
    return render(request, "app/dashboard.html", context)


def profile(request, user_id):
    user = request.user
    user_from_job = User.objects.get(pk=user_id)
    email_form = EmailChangeForm(user)
    password_form = SetPasswordForm(user)
    accepted_jobs = Job.objects.filter(
        Q(user=user_from_job), Q(is_assigned=True)
    )  # jobs that are from user
    completed_jobs = Job.objects.filter(Q(user=user_from_job), Q(is_completed=True))

    translators_bid = JobBid.objects.filter(Q(bid_user=user_from_job))
    translator_assigned_jobs = Job.objects.filter(
        Q(translator=user_from_job), Q(is_assigned=True)
    )  # jobs that are NOT from user
    translator_completed_jobs = Job.objects.filter(
        Q(translator=user_from_job), Q(is_completed=True)
    )

    context = {
        "user": user,
        "user_from_jobs": user_from_job,
        "email_form": email_form,
        "password_form": password_form,
        "accepted_jobs": accepted_jobs,
        "completed_jobs": completed_jobs,
        "translator_bids": translators_bid,
        "translator_assigned_jobs": translator_assigned_jobs,
        "translator_completed_jobs": translator_completed_jobs,
    }
    return render(request, "app/profile.html", context)


@login_required()
def email_change(request, user_id):
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

        return HttpResponseRedirect(reverse("app:profile", args=[user_id]))
    else:
        context = {"user": user, "email_form": form, "password_form": password_form}
        return render(request, "app/profile.html", context)


@login_required()
def change_password(request, user_id):
    user = request.user
    email_form = EmailChangeForm(user)
    if request.method == "POST":
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect("login")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        context = {"user": user, "form": form, "email_form": email_form}
        return HttpResponseRedirect(reverse("app:profile", args=[user_id]))
    else:
        form = SetPasswordForm(user)

        context = {"user": user, "form": form, "email_form": email_form}
        return render(request, "app/profile.html", context)


def post_job(request):
    user = request.user
    form = JobForm(initial={"job_field": "ART"})
    if request.method == "POST":
        form = JobForm(request.POST, user=user)
        if form.is_valid():
            job_post = Job.objects.create(
                user=user,
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
        form = JobForm()
    return render(request, "app/post_job.html", {"form": form})


def jobs(request):
    user = request.user
    jobs = Job.objects.all().filter(
        ~Q(user=user), Q(is_assigned=False), Q(is_completed=False)
    )

    context = {
        "user": user,
        "jobs": jobs,
    }
    return render(request, "app/jobs.html", context)


def job_bid(request, job_id):
    user = request.user
    form = JobBidForm(user=user, initial={"bid": 0.0})
    job = Job.objects.get(pk=job_id)
    if request.method == "POST":
        form = JobBidForm(request.POST, user=user, job=job)
        if form.is_valid():
            job_bid = JobBid.objects.create(
                bid_user=user, job=job, bid=form.cleaned_data.get("bid")
            )
            return HttpResponseRedirect(reverse("app:jobs", args=[]))
        else:
            return render(request, "app/bid.html", {"form": form, "job": job})
    else:
        context = {
            "user": user,
            "job": job,
            "form": form,
        }
    return render(request, "app/bid.html", context)


def message_user(request, job_id):
    user = request.user
    job = get_object_or_404(Job, pk=job_id)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message.objects.create(
                from_user=request.user,
                to_user=job.user,
                job=job,
                text=form.cleaned_data.get("text"),
            )
            return HttpResponseRedirect(reverse("app:jobs", args=[]))
        else:
            context = {"user": user, "job": job, "form": form}
            return render(request, "app/message_page.html", context)
    else:
        form = MessageForm()
        context = {"user": user, "job": job, "form": form}
    return render(request, "app/message_page.html", context)


def job_status(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {
        "job": job,
    }
    return render(request, "app/job_status.html", context)


def dispute_job(request, job_id):
    user = request.user
    job = get_object_or_404(Job, pk=job_id)
    form = DisputeJobForm(instance=job)

    context = {
        "job": job,
        "user": user,
        "form": form,
    }

    if request.method == "POST":
        form = DisputeJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("app:dashboard", args=[]))
        else:
            context = {
                "job": job,
                "user": user,
                "form": form,
            }
            return render(request, "app/dispute_job.html", context)
    else:
        form = DisputeJobForm(instance=job)
        context = {
            "job": job,
            "user": user,
            "form": form,
        }
    return render(request, "app/dispute_job.html", context)


def view_translation(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {
        "job": job,
    }
    return render(request, "app/view_translation.html", context)

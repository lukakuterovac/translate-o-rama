from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserProfileSignupForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy


def register(request):
    if request.method == "POST":
        signup_form = UserSignupForm(request.POST)
        profile_form = UserProfileSignupForm(request.POST)
        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            user.refresh_from_db()
            profile_form = UserProfileSignupForm(
                request.POST, instance=user.userprofile
            )
            profile_form.full_clean()
            profile_form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            context = {
                "signup_form": signup_form,
                "profile_form": profile_form,
            }
    else:
        signup_form = UserSignupForm()
        profile_form = UserProfileSignupForm(initial={"is_translator": False})
        context = {
            "signup_form": signup_form,
            "profile_form": profile_form,
        }
    return render(
        request=request,
        template_name="registration/signup.html",
        context=context,
    )


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid uemail or password.")
    form = UserLoginForm()
    return render(
        request=request, template_name="main/login.html", context={"login_form": form}
    )

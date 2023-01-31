from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


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
    context = {
        "user": user,
    }
    return render(request, "app/profile.html", context)

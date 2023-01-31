from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    context = {}
    return render(request, "app/home.html", context)


def dashboard(request):
    if request.user.is_superuser:
        return HttpResponseRedirect("", "")
    return HttpResponse("/")

from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("sign-up", views.register, name="signup"),
]

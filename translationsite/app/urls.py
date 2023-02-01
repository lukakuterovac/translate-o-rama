from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("post_job", views.post_job, name="post_job"),
]

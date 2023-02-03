from django.urls import path, include
from . import views
from django.urls import include
from .forms import EmailChangeForm

app_name = "app"
urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("post_job", views.post_job, name="post_job"),
    path(
        "profile/<int:user_id>/password_change",
        views.change_password,
        name="new_password",
    ),
    path("profile/<int:user_id>/email_change", views.email_change, name="new_email"),
    path("jobs", views.jobs, name="jobs"),
    path("jobs/job_bid/<int:job_id>", views.job_bid, name="jobs_bid"),
    path("jobs/<int:job_id>", views.message_user, name="message_user"),
]

from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile", views.profile, name="profile"),
    path("post_job", views.post_job, name="post_job"),
    path("profile/password_change", views.change_password, name="new_password"),
    path("profile/email_change", views.change_email, name="new_email"),
]

from django.contrib import admin

from .models import UserProfile, Job, Message

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Job)
admin.site.register(Message)

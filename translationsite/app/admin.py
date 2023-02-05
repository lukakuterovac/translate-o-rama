from django.contrib import admin

from .models import UserProfile, Job, Message, JobBid, Rating, Dispute

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Job)
admin.site.register(Message)
admin.site.register(JobBid)
admin.site.register(Rating)
admin.site.register(Dispute)

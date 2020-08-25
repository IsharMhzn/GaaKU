from django.contrib import admin
from .models import Profile, Notification, History, Updates

# Register your models here.
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(History)
admin.site.register(Updates)
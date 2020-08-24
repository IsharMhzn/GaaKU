from django.contrib import admin
from .models import Profile, Notification, History

# Register your models here.
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(History)
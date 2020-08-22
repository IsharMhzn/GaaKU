from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('profile/notification', views.notificationview, name="notification")
]

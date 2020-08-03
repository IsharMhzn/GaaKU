from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('Home.urls')),
    path('', include('Account.urls')),
    path('admin/', admin.site.urls),
]
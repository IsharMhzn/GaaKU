from django.urls import path
from .views import login_view, logout_user, signup_view, activate

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('confirm/<userid>', activate, name='activate')
]
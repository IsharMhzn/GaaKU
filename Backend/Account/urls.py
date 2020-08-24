from django.urls import path
from .views import login_view, logout_user, signup_view, activate, forgot_password, password_reset, profile, historyview

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('confirm/<userid>', activate, name='activate'),
    path('forgot/', forgot_password, name='forgot password'),
    path('reset/<userid>', password_reset, name='pasword_reset'),
    path('profile/', profile, name='profile'),
    path('profile/history', historyview, name='trans-history')
]

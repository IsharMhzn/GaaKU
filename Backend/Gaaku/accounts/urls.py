from django.urls import path
from .views import signup_page_view, login_page_view, logout_user, activate

urlpatterns = [
    path('signup', signup_page_view, name='signup'),
    path('login', login_page_view, name='login'),
    path('logout', logout_user, name='logout'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    	activate, name='activate'),
]
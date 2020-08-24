from django.urls import path
from .views import (login_view, logout_user,
                    signup_view, activate,
                    forgot_password, password_reset,
                    profile, SellListView,
                    SellDetailView, SellCreateView,
                    SellUpdateView, SellDeleteView
                    )
urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('confirm/<userid>', activate, name='activate'),
    path('forgot/', forgot_password, name='forgot password'),
    path('reset/<userid>', password_reset, name='pasword_reset'),
    path('profile/', profile, name='profile'),
    path('profile/sell/<str:username>',
         SellListView.as_view(), name='myproducts'),
    path('profile/sell/<int:pk>/', SellDetailView.as_view(), name='sell-detail'),
    path('profile/sell/new/', SellCreateView.as_view(), name='sell'),
    path('profile/sell/<int:pk>/update',
         SellUpdateView.as_view(), name='sell-update'),
    path('profile/sell/<int:pk>/delete',
         SellDeleteView.as_view(), name='sell-delete')


]

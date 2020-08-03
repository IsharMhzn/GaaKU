from django.urls import path
from .views import Homepage, Aboutpage, Wishlistpage

urlpatterns = [
	path('', Homepage, name='home'),
	path('about/', Aboutpage, name='about'),
	path('wishlist/', Wishlistpage, name='wishlist')
]
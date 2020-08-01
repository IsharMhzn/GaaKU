from django.urls import path
from .views import Homepage, Aboutpage, Wishlistpage

urlpatterns = [
	path('', Homepage, name='Gaaku home'),
	path('about/', Aboutpage, name='Gaaku about'),
	path('wishlist/', Wishlistpage, name='Gaaku wishlist')
]
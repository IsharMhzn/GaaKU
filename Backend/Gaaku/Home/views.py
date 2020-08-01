from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Homepage(request):
	return render(request, 'home/homepage.html')

def Aboutpage(request):
	return render(request, 'home/about.html')

def Wishlistpage(request):
	return render(request, 'home/wishlist.html')
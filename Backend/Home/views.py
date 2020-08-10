from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products

# Create your views here.
def index(request):
    products=Products.objects.all()[::-1][:10]
    return render(request,'home/index.html',{'products':products})

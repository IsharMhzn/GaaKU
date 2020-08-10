from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def index(request):
    products=Products.objects.all()
    print(products);
    return render(request,'products/index.html',{'products':products})
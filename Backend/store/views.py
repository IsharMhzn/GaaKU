from django.shortcuts import render

from django.views.generic import ListView
from .models import Product

# Create your views here.
class ProductView(ListView):
    model=Product

def pmainpage(request):
    products = Product.objects.all()
    context = {'products':products}
    print("P is called")
    return render(request, 'pmainpage.html', context)

def Description(request,id):
    products = Product.objects.filter(id=id)
    print(products)
    print('D is called')
    context={'products':products}
    return render(request, 'Description.html', context)

def Landingpage(request):
    context = {}
    return render(request, 'landing.html')

def category(request,category):
    products=Product.objects.filter(category=category)
    return render(request,'pmainpage.html',{'products':products})
    
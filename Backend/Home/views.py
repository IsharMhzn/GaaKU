from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()[::-1][:10]
    print(products)
    return render(request,'home/index.html',{'products':products})

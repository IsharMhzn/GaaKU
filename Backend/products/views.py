from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def index(request):
    products=Products.objects.all()
    return render(request,'products/index.html',{'products':products})

def category_view(request,category):
    products=Products.objects.filter(category=category)
    return render(request,'products/index.html',{'products':products});

def search(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
    if q:
        products=Products.objects.filter(category=q)
        return render(request,'products/index.html',{'products':products})
    else:
        return HttpResponse('No Products Search')

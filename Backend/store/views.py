from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Product

# Create your views here.
class pmainpage(ListView):
    model=Product
    template_name = 'pmainpage.html'

# def pmainpage(request):
#     products = Product.objects.all()
#     context = {'products':products}
#     print("P is called")
#     return render(request, 'pmainpage.html', context)
class Description(DetailView):
    model =Product
    template_name = 'Description.html'


# def Description(request,id):
#     products = Product.objects.filter(id=id)
#     print(products)
#     print('D is called')
#     context={'products':products}
#     return render(request, 'Description.html', context)

def Landingpage(request):
    context = {}
    return render(request, 'landing.html')

def category(request,category):
    products=Product.objects.filter(category=category)
    return render(request,'pmainpage.html',{'products':products})

def search(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
    if q:
        products=Product.objects.filter(name__icontains=q) | Product.objects.filter(category__icontains=q)   
        print(products)
        return render(request,'pmainpage.html',{'products':products})
    else:
        return HttpResponse('EMPTY')
    
    
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Product , Customer ,OrderItem,Order
from django.utils import timezone
from django.shortcuts import redirect
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


def add_to_whishlist(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.user.is_authenticated:
        try:
            order_item, created = OrderItem.objects.get_or_create(
                item=item,
                user=request.user,
                ordered=False
            )
            order_qs = Order.objects.filter(user=request.user, ordered=False)
            if order_qs.exists():
                order = order_qs[0]
                # check if the order item is in the order
                if order.items.filter(item__pk=item.pk).exists():
                    order_item.quantity += 1
                    order_item.save()
                    # messages.info(request, "This item quantity was updated.")
                    return redirect("Description",pk=pk )
                else:
                    order.items.add(order_item)
                    # messages.info(request, "This item was added to your cart.")
                    return redirect("Description",pk=pk )
            else:
                ordered_date = timezone.now()
                order = Order.objects.create(
                    user=request.user, ordered_date=ordered_date,name=request.item.name)
                order.items.add(order_item)
                # messages.info(request, "This item was added to your cart.")
                return redirect("Description",pk=pk )
        except request.user.DoesNotExist:
             return redirect("Description",pk=pk )
                
    else:
        print("Your are not  allowed")
    
    
        





# def Description(request,id):
#     products = Product.objects.filter(id=id)
#     print(products)
#     print('D is called')
#     context={'products':products}
    #   if request.POST.get('submit'):

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
    
    
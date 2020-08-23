from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
<<<<<<< HEAD
from .models import Product , Customer ,OrderItem,Order
from django.utils import timezone
from django.shortcuts import redirect
=======
from .models import Product, Comment
from Account.models import Notification

>>>>>>> 30a2ec9e1ea3663a0841d91595d1edda7cfaeee6
# Create your views here.
class pmainpage(ListView):
    model=Product
    template_name = 'pmainpage.html'
<<<<<<< HEAD
 
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
=======

# def pmainpage(request):
#     products = Product.objects.all()
#     context = {'products':products}
#     print("P is called")
#     return render(request, 'pmainpage.html', context)

# class Description(DetailView):
#     model =Product
#     template_name = 'Description.html'


def Description(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        content = request.POST.get('comment-content')
        commentid = request.POST.get('Commentid')
        if content != '':
            if commentid is not None:
                c = Comment(content=content, user=request.user, post=product, reply=Comment.objects.get(id=commentid))
            else:
                c = Comment(content=content, user=request.user, post=product)
            c.save()
            n = Notification(user=request.user, post=product, comment=c)
            n.save()

    comments = Comment.objects.filter(post=product, reply=None)
    replies = Comment.objects.filter(post=product).exclude(reply=None)
    return render(request, 'Description.html', {'comments':comments,'replies': replies, 'object':product})
>>>>>>> 30a2ec9e1ea3663a0841d91595d1edda7cfaeee6

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
    
def commentview(request):
    if request.method == 'POST':
        content = request.POST.get('comment-content')
        c = Comment(content=content, user=request.user)
        c.save()
    comments = Comment.objects.all()
    return render(request, 'comment.html', {'comments':comments})
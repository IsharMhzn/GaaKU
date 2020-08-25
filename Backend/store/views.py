from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Product, Customer, WishlistItem, Wishlist, Comment
from django.utils import timezone
from django.shortcuts import redirect
from Account.models import Notification, NotificationCount
from django.contrib import messages


# Create your views here.


class pmainpage(ListView):
    model = Product
    template_name = 'pmainpage.html'

# def pmainpage(request):
#     products = Product.objects.all()
#     context = {'products':products}
#     print("P is called")
#     return render(request, 'pmainpage.html', context)

# class Description(DetailView):
#     model =Product
#     template_name = 'Description.html'


def add_to_whishlist(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.user.is_authenticated:
        try:
            order_item, created = WishlistItem.objects.get_or_create(
                item=item,
                user=request.user,
                ordered=False
            )
            order_qs = Wishlist.objects.filter(
                user=request.user, ordered=False)
            if order_qs.exists():
                order = order_qs[0]
                # check if the order item is in the order
                if order.items.filter(item__pk=item.pk).exists():
                    order_item.quantity += 1
                    order_item.save()
                    messages.info(
                        request, "This item's quantity was updated in your wishlist. Please check your Profile.")
                    return redirect("Description", pk=pk)

                else:
                    order.items.add(order_item)
                    messages.info(
                        request, "This item was added to your wishlist. Please check your Profile.")
                    return redirect("Description", pk=pk)
            else:
                ordered_date = timezone.now()
                order = Wishlist.objects.create(
                    user=request.user, ordered_date=ordered_date)
                order.items.add(order_item)
                messages.info(
                    request, "This item was added to your wishlist. Please check your Profile.")
                return redirect("Description", pk=pk)
        except request.user.DoesNotExist:
            return redirect("Description", pk=pk)

    else:
        print("Your are not  allowed")


def Description(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        content = request.POST.get('comment-content')
        commentid = request.POST.get('Commentid')
        if content != '':
            if commentid is not None:
                c = Comment(content=content, user=request.user,
                            post=product, reply=Comment.objects.get(id=commentid))
            else:
                c = Comment(content=content, user=request.user, post=product)
            c.save()
            n = Notification(user=request.user, post=product, comment=c)
            n.save()

            try:
                if not product.user == request.user:
                    notifc = NotificationCount.objects.get_or_create(user=product.user)[
                        0]
                else:
                    notifc = NotificationCount.objects.get_or_create(user=c.reply.user)[
                        0]
                notifc.old += 1
                notifc.seen = False
                notifc.save()
            except AttributeError:
                print('ignore this')

    if request.user == product.user:
        comments = Comment.objects.filter(post=product, reply=None)
    else:
        comments = Comment.objects.filter(
            post=product, reply=None, user=request.user)

    if request.user == product.user:
        replies = Comment.objects.filter(post=product).exclude(reply=None)
    else:
        replies = Comment.objects.filter(post=product).exclude(reply=None)
    return render(request, 'Description.html', {'comments': comments, 'replies': replies, 'object': product})


# def Description(request,id):
#     products = Product.objects.filter(id=id)
#     print(products)
#     print('D is called')
#     context={'products':products}
    #   if request.POST.get('submit'):

#     return render(request, 'Description.html', context)

# def pmainpage(request):
#     products = Product.objects.all()
#     context = {'products':products}
#     print("P is called")
#     return render(request, 'pmainpage.html', context)

# class Description(DetailView):
#     model =Product
#     template_name = 'Description.html'


def Landingpage(request):
    context = {}
    return render(request, 'landing.html')


def category(request, category):
    products = Product.objects.filter(category=category)
    print(products)
    return render(request, 'pmainpage.html', {'object_list': products})


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(
            name__icontains=q) | Product.objects.filter(category__icontains=q)
        print(products)
        return render(request, 'pmainpage.html', {'object_list': products})
    else:
        return HttpResponse('EMPTY')


def commentview(request):
    if request.method == 'POST':
        content = request.POST.get('comment-content')
        c = Comment(content=content, user=request.user)
        c.save()
    comments = Comment.objects.all()
    return render(request, 'comment.html', {'comments': comments})

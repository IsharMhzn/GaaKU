from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Product, Comment
from Account.models import Notification

# Create your views here.
class pmainpage(ListView):
    model=Product
    template_name = 'pmainpage.html'

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
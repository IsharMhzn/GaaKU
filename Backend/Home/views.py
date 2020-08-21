from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from Account.models import Notification

# Create your views here.
def index(request):
    products=Product.objects.all()[::-1][:10]
    print(products)
    return render(request,'home/index.html',{'products':products})

def profile(request):
    notifications = Notification.objects.all()[::-1]
    notifs = list()
    for n in notifications:
        if n.user != request.user:
            if n.comment.reply:
                if n.comment.reply.user == request.user:
                    notifs.append(n)
                    continue
            if n.post.user == request.user:
                notifs.append(n)
    print(notifs)
    return render(request, 'home/profile.html', {'notifs':notifs})
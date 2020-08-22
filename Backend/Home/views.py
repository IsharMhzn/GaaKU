from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product
from Account.models import Notification

# Create your views here.
def index(request):
    products=Product.objects.all()[::-1][:10]
    print(products)
    return render(request,'home/index.html',{'products':products})

def notificationview(request):
    notifications = Notification.objects.all()[::-1]
    notifs = list()
    if request.user.is_authenticated:
        for n in notifications:
            if n.user != request.user:
                if n.comment.reply:
                    if n.comment.reply.user == request.user:
                        notifs.append(n)
                        continue
                if n.post.user == request.user:
                    notifs.append(n)
        print(notifs)
        return render(request, 'home/notification.html', {'notifs':notifs})
    return redirect('login')
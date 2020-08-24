from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product
from Account.models import Notification, NotificationCount
import random
# Create your views here.
def index(request):
    products=Product.objects.all()[::-1][:10]
    featuredProducts=Product.objects.all()
    negotiableProducts=Product.objects.filter(negotiation=True)
    
    randomFeaturedProducts=([random.choice(featuredProducts) for i in range(len(featuredProducts))])
    resultFeatuedProducts= []
    for item in randomFeaturedProducts:
        if not item in resultFeatuedProducts:
            resultFeatuedProducts.append(item)
    resultFeatuedProducts=resultFeatuedProducts[:len(resultFeatuedProducts)//4*4]

    randomNegotiableProducts=[random.choice(negotiableProducts) for i in range(len(negotiableProducts))]
    resultNegoitableProduct=[]
    for item in randomNegotiableProducts:
        if not item in resultNegoitableProduct:
            resultNegoitableProduct.append(item)
    resultNegoitableProduct=resultNegoitableProduct[:10]

    return render(request,'home/index.html',{'products':products, 'featuredProducts':resultFeatuedProducts,'negotiable':resultNegoitableProduct});

def notificationview(request):
    notifc = NotificationCount.objects.get_or_create(user=request.user)[0]
    if not notifc.seen:
        notifc.seen = True
        notifc.updated = notifc.old
        notifc.save()
    print(notifc.seen, notifc.user)
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
        return render(request, 'home/notification.html', {'notifs':notifs})
    return redirect('login')
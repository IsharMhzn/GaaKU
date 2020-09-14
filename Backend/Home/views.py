from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product
from Account.models import Notification, NotificationCount, Updates, Testimony
import random
# Create your views here.
def index(request):
    subscribed = False
    notifs = []
    newNotif = None
    allproducts = []
    if request.user.is_authenticated:
        try:
            subscribed = Updates.objects.get(user=request.user)
        except: 
            pass
        notifc = NotificationCount.objects.get_or_create(user=request.user)[0]
        newNotif = not notifc.seen
        notifc = NotificationCount.objects.get_or_create(user=request.user)[0]
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
        try:
            u = Updates.objects.get(user=request.user)
            allpros = Product.objects.all()[::-1]
            for p in allpros:
                if p.timestamp:
                    if u.timestamp < p.timestamp:
                        if p.user != request.user:
                            allproducts.append(p)
        except:
            allproducts = None
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
    
    testimonials = [random.choice(Testimony.objects.all()) for i in range(3)]
    print(testimonials)

    context = {'products':products, 
               'featuredProducts':resultFeatuedProducts,
               'negotiable':resultNegoitableProduct,
               'notifs':notifs,
               'updates':allproducts,
               'newNotif': newNotif,
               'subscribed': subscribed,
               'testimonials': testimonials}
    return render(request,'home/index.html', context)


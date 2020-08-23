from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from Account.models import Notification
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
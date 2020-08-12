from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone_no=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.IntegerField()
    discription = models.TextField()
    negotiation = models.BooleanField(default=False,null=True,blank=False)
    img = models.ImageField(upload_to='pics',null=True,blank=True)
    contact_info = models.TextField()
    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url= self.img.url
        
        except:
            url =''
        return url

     
    
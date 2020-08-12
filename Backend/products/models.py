from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    category_id=models.IntegerField()
    price=models.IntegerField()
    image_url=models.CharField(max_length=2083)
    
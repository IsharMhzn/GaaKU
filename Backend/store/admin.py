from django.contrib import admin

# Register your models here.
from .models import Customer,Product,OrderItem,Order

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','category')

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
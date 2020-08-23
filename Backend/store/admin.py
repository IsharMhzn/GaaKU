from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Customer,Product,OrderItem,Order
=======
from .models import Customer,Product, Comment
>>>>>>> 30a2ec9e1ea3663a0841d91595d1edda7cfaeee6

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','category')

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
<<<<<<< HEAD
admin.site.register(OrderItem)
admin.site.register(Order)
=======
admin.site.register(Comment)
>>>>>>> 30a2ec9e1ea3663a0841d91595d1edda7cfaeee6

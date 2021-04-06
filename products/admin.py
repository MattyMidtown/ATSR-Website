from django.contrib import admin

# Register your models here.
from .models import Product, Orderproduct, Orders, OrderProductrel

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Orderproduct)
admin.site.register(OrderProductrel)

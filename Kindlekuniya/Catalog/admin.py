from django.contrib import admin

from .models import Product, Catagory, CatagoryMap, Stock

admin.site.register(Product)
admin.site.register(Catagory)
admin.site.register(CatagoryMap)
admin.site.register(Stock)

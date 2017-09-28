from django.contrib import admin
from .models import Product, Catagory, CatagoryMap, Stock

class CatagoryMapInline(admin.TabularInline):
    model = CatagoryMap
    extra = 1

class StockInline(admin.TabularInline):
    model = Stock
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [CatagoryMapInline, StockInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Catagory)
admin.site.register(Stock)

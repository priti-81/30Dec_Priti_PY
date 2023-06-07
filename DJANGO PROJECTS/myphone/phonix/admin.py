from django.contrib import admin
from .models import product,productdetails

# Register your models here.
""" class productData(admin.ModelAdmin):
    list_display=['productname']

class productdata2(admin.ModelAdmin):
    list_display=['product','productprice','productimage','productmodel','productRAM'] """

admin.site.register(product)
admin.site.register(productdetails)


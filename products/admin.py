from django.contrib import admin
from products.models import Product

admin.site.register(Product)


# @admin.register(Product)
# class AdminProducts(admin.ModelAdmin):
#     model = Product
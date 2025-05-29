from django.shortcuts import render
import os
from Borchimash.settings import BASE_DIR, STATIC_URL
from django.http import HttpRequest
from products.models import Product, Category

FILES_ROOT = os.path.join(STATIC_URL, 'models')

def index(req: HttpRequest):
    return render(req, "products/index.html", {'categories': Category.objects.all()})

def product(req: HttpRequest, category: int):
    products = Product.objects.filter(category=category)
    category_name = Category.objects.get(pk=category)
    return render(req, 'products/products/product.html', {"title": category_name, "products": products})
        
from django.shortcuts import render
import os
from Borchimash.settings import BASE_DIR, STATIC_URL
from django.http import HttpRequest
from products.models import Product, Category

FILES_ROOT = os.path.join(STATIC_URL, 'models')

def index(req: HttpRequest):
    return render(req, "products/index.html", {'categoies': Category.objects.all()})

# def add(request: HttpRequest):
#     if request.method == "POST":
        
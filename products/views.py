from django.shortcuts import render
import os
from Borchimash.settings import BASE_DIR, STATIC_URL
from django.http import HttpRequest
from products.models import Product, Category
from django.core.paginator import Paginator
from main.paginator import new_paginator

FILES_ROOT = os.path.join(STATIC_URL, "models")


def index(req: HttpRequest):
    category = Category.objects.all()
    # paginator = Paginator(category, 6)
    # if "page" in req.GET:
    #     page_num = req.GET["page"]
    # else:
    #     page_num = 1
    # page = paginator.get_page(page_num)
    page = new_paginator(req, 6, category)
    return render(
        req, "products/index.html", {"page": page, "categories": page.object_list}
    )


def product(req: HttpRequest, category: int):
    products = Product.objects.filter(category=category)
    category_name = Category.objects.get(pk=category)

    return render(
        req,
        "products/products/product.html",
        {
            "title": category_name,
            "products": products,
        },
    )

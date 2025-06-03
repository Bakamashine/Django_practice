from django.shortcuts import render
import os
from Borchimash.settings import BASE_DIR, STATIC_URL
from django.http import HttpRequest
from products.models import Product, Category
from django.core.paginator import Paginator
from main.paginator import new_paginator
from django.views import View

FILES_ROOT = os.path.join(STATIC_URL, "models")


def index(req: HttpRequest):
    category = Category.objects.all()
    page = new_paginator(req, category)
    return render(
        req, "products/index.html", {"page": page, "categories": page.object_list}
    )


def product(req: HttpRequest, category: int):
    products = Product.objects.filter(category=category)
    category = Category.objects.get(pk=category)
    page = new_paginator(req, products)

    return render(
        req,
        "products/products/product.html",
        {
            "page": page,
            'category': category,
            "products": page.object_list,
        },
    )

class ProductDetail(View):
    model = Product
    template_name ="products/products/detail.html"

    def dispatch(self, request, product: int, *args, **kwargs):
        if request.method == "GET":
            return render(
                request,
                self.template_name,
                {"product": self.model.objects.get(pk=product)}
            )

class ProductDetail3D(ProductDetail):
    template_name = "products/products/3d.html"

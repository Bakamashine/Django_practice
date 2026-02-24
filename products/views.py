import os

from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from rest_framework import generics

from Borchimash.settings import STATIC_URL
from main.paginator import new_paginator
from products.serializers import *

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
    template_name = "products/products/detail.html"

    def dispatch(self, request, product: int, *args, **kwargs):
        if request.method == "GET":
            return render(
                request,
                self.template_name,
                {"product": self.model.objects.get(pk=product)}
            )


class ProductDetail3D(ProductDetail):
    template_name = "products/products/3d.html"


class CategoryDetailApi(generics.RetrieveAPIView):
    serializer_class = CategorySerializersOne
    queryset = Category.objects.all()
    lookup_field = "id"


class CategoryApi(generics.ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class ProductApi(generics.ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    lookup_field = "category_id"


class ProductDetailApi(generics.RetrieveAPIView):
    serializer_class = ProductSerializersOne
    queryset = Product.objects.all()
    lookup_field = "id"


class OnlyFileProductApi(ProductDetailApi):
    serializer_class = OnlyFileProductSerializers

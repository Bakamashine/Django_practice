from django.urls import path
from products.views import index, product, product_detail

urlpatterns = [
    path("category", index, name="category"),
    path("category/<int:category>", product, name="products"),
    path("category/product/<int:product>", product_detail, name="product_detail")
]

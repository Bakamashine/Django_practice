from django.urls import path
from products.views import index, product

urlpatterns = [
    path("category", index, name="category"),
    path("category/<int:category>", product, name="products")
]

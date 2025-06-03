from django.urls import path
from products.views import index, product, ProductDetail, ProductDetail3D

urlpatterns = [
    path("category", index, name="category"),
    path("category/<int:category>", product, name="products"),
    # path("category/product/<int:product>", product_detail, name="product_detail")
    path("category/product/<int:product>", ProductDetail.as_view(), name="product_detail"),
    path("category/product/3d/<int:product>", ProductDetail3D.as_view(), name="product_detail_3d"),
]

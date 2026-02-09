from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from news.views import NewsViewApi, OneNewsViewApi, YearNewsViewApi
from main.views import FeedbackViewApi, FormViewSet
from RegAuth.views import RegisterUserApi, GetUserApi
from products.views import *

router = routers.DefaultRouter()
# router.register(r'news', NewsViewApi)   
router.register(r"form", FormViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),

    # App routes
    path("", include("main.urls")),
    path("", include("RegAuth.urls")),
    path("products/", include("products.urls")),
    path("news/", include("news.urls")),

    # DRF router
    path("api/", include(router.urls)),

    # Custom API endpoints
    path("api/feedback", FeedbackViewApi.as_view(), name="feedback"),
    
    # News
    path("api/news/", NewsViewApi.as_view(), name="news-list"),
    path("api/news/<int:id>/", OneNewsViewApi.as_view(), name="news-detail"),
    path("api/news/year/<int:year>/", YearNewsViewApi.as_view(), name='news-years'),

    # Category
    path("api/category/", CategoryApi.as_view(), name="category-list"),
    path("api/category/<int:id>/", CategoryDetailApi.as_view(), name="category-detail"),

    # Product
    path("api/category/product/<int:category_id>/", ProductApi.as_view(), name="product-list-by-category"),
    path("api/product/<int:id>", ProductDetailApi.as_view(), name="product-detail"),
    path("api/product/file_only/<int:id>", OnlyFileProductApi.as_view(), name="product-only-file"),

    # Auth view api
    path("api/register", RegisterUserApi.as_view(), name="register"),
    path("api/getuser", GetUserApi.as_view(), name="get-user"),

    # Auth
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),

    # DRF login
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),

    # Summernote
    path("summernote", include("django_summernote.urls")),
]

# Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
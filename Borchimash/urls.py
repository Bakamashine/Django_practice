"""
URL configuration for Borchimash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
    path("api/news/", NewsViewApi.as_view(), name="news-list"),
    path("api/news/<int:id>/", OneNewsViewApi.as_view(), name="news-detail"),
    path("api/news/years/<int:year>/", YearNewsViewApi.as_view(), name='news-years'),
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
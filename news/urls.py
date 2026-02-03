from django.urls import path
from news.views import detail, year
from rest_framework import routers
from .views import NewsViewSet


urlpatterns = [
    path("<int:one_news>", detail, name="news_detail"),
    path("year/<int:year>", year, name="year")
]

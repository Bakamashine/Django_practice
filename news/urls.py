from django.urls import path
from news.views import detail, year

urlpatterns = [
    path("<int:one_news>", detail, name="news_detail"),
    path("year/<int:year>", year, name="year")
]

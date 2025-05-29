from django.urls import path
from news.views import detail

urlpatterns = [
    path("<int:one_news>", detail, name="news_detail")
]

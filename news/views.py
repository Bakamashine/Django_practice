from django.shortcuts import render
from django.http import HttpRequest
from news.models import News
from typing import List
from datetime import datetime
from rest_framework import viewsets, permissions, generics
from .serializers import *


def detail(req: HttpRequest, one_news: int):
    news = News.objects.get(pk=one_news)
    return render(req, "news/detail.html", {"one_news": news})

def year(req: HttpRequest, year: int):
    news = News.objects.filter(date__year__exact=year).order_by('-date')
    return render(req, 'news/year.html', {"news": news, "year": year})


class NewsViewApi(generics.ListAPIView):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer

class OneNewsViewApi(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = OneNewsSerilizer
    lookup_field = "id"

class YearNewsViewApi(generics.ListAPIView):

    serializer_class = NewsSerializer

    def get_queryset(self):
        year = self.kwargs["year"]
        return News.objects.filter(date__year__exact=year).order_by("-date")

    # queryset = News.objects.all()
    # serializer_class = NewsSerializer
    # lookup_field = "years"
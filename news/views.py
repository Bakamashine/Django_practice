from django.shortcuts import render
from django.http import HttpRequest
from news.models import News
from typing import List
from datetime import datetime


def detail(req: HttpRequest, one_news: int):
    news = News.objects.get(pk=one_news)
    return render(req, "news/detail.html", {"one_news": news})

def year(req: HttpRequest, year: int):
    news = News.objects.filter(date__year__exact=year).order_by('-date')
    return render(req, 'news/year.html', {"news": news, "year": year})
from django.shortcuts import render
from news.models import News

def index(req):
    news = News.objects.all().values("date", 'text', 'id').order_by("-date")[:4]
    return render(req, "main/index.html", {"news": news})

def about_us(req):
    return render(req, 'main/about_us.html')

def contacts(req):
    return render(req, 'main/contacts.html')
from django.shortcuts import render
from django.http import HttpRequest
from news.models import News, Images
from typing import List
from datetime import datetime


def detail(req: HttpRequest, one_news: int):
    news = News.objects.get(pk=one_news)
    images: List[Images] = news.images.all()
    years = []
    dates = News.objects.all().values('date')

    # TODO: Работает..
    for n in dates:
        try: 
            my_date = datetime.strftime(n['date'], "%Y")
            if years.index(my_date):
                years.append(my_date)
        except ValueError:
            years.append(my_date)
        except:
            continue
        

    return render(req, "news/detail.html", {"one_news": news, "images": images, "years": years})

def year(req: HttpRequest, year: int):
    # news = News.objects.filter(date=)
    return render(req, 'news/year.html')
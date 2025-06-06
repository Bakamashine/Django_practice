from django.shortcuts import render,redirect
from news.models import News
from django.http import HttpRequest
from main.forms import FeedbackForm
from main.models import Feedback
from products.models import Category
from django.contrib.auth.decorators import login_required

def index(req):
    news = News.objects.all().values("date", 'title', 'id').order_by("-date")[:4]
    categories = Category.objects.all().values('id', "name")[:30]
    return render(req, "main/index.html", {"news": news, "categories": categories})

def about_us(req):
    return render(req, 'main/about_us.html')

def contacts(req):
    return render(req, 'main/contacts.html')

def test(req):
    return render(req, 'main/test.html')

@login_required
def feedback(req: HttpRequest):
    if req.method == "GET":
        return render(req, 'main/feedback.html', {'form': FeedbackForm})
    elif req.method == "POST":
        form = FeedbackForm(req.POST)
        if form.is_valid(): 
            text = form.cleaned_data['text']
            phone = form.cleaned_data['phone']
            Feedback.objects.create(text=text, phone=phone, user=req.user)
            return redirect("main")
        else:
            return render(req, 'main/feedback.html', {'form': form})

def blanks(req: HttpRequest):
    return render(req, 'main/blanks.html')

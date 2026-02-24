from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework import viewsets, generics, permissions, response, status

from main.forms import FeedbackForm
from main.models import Feedback, Forms
from news.models import News
from products.models import Category
from .serializers import FeedbackSerializer, FormSerializer


def index(req):
    news = News.objects.all().values("date", "title", "id").order_by("-date")[:4]
    categories = Category.objects.all().values("id", "name")[:30]
    return render(req, "main/index.html", {"news": news, "categories": categories})


def about_us(req):
    return render(req, "main/about_us.html")


def contacts(req):
    return render(req, "main/contacts.html")


# def test(req):
#     return render(req, "main/test.html")


@login_required
def feedback(req: HttpRequest):
    if req.method == "GET":
        return render(req, "main/feedback.html", {"form": FeedbackForm})
    elif req.method == "POST":
        form = FeedbackForm(req.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            phone = form.cleaned_data["phone"]
            Feedback.objects.create(text=text, phone=phone, user=req.user)
            return redirect("main")
        else:
            return render(req, "main/feedback.html", {"form": form})
    return None


def blanks(req: HttpRequest):
    return render(req, "main/blanks.html")


class FormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Forms.objects.all()
    serializer_class = FormSerializer


class FeedbackViewApi(generics.ListCreateAPIView):
    queryset = Feedback.objects.all().order_by("-date")
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        feedback_ser = self.serializer_class(data=request.data)
        if feedback_ser.is_valid():
            new_feedback = Feedback.objects.create(
                user=request.user,
                text=feedback_ser.data["text"],
                phone=feedback_ser.data["phone"],
            )

            new_feedback.save()
            return response.Response(status=status.HTTP_201_CREATED)
        return super().post(request, *args, **kwargs)

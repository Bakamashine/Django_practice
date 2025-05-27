from django.urls import path
from main.views import index
from django.shortcuts import render

urlpatterns = [
    path("", index, name="main"),
    path("test/", lambda req: render(req, "main/test.html")),
]

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from RegAuth.views import CustomLoginView, CustomRegisterView

urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login")
] 

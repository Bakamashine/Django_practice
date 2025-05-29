from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from RegAuth.views import CustomLoginView, CustomRegisterView, accept_email, accept_email2, CustomLogout

urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("acceptEmail/", accept_email, name="acceptEmail"),
    path("accept/<str:token>/<str:uid>/", accept_email2, name="acceptEmail2"),
    path("logout", CustomLogout.as_view(), name="logout"),
] 

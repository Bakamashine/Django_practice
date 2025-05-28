from django.urls import path
from main.views import index, about_us, contacts

urlpatterns = [
    path("", index, name="main"),
    path("about_us/", about_us, name="about_us"),
    path("contacts/", contacts, name='contacts')
]

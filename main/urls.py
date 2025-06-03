from django.urls import path
from main.views import index, about_us, contacts, test, feedback, blanks

urlpatterns = [
    path("", index, name="main"),
    path("about_us/", about_us, name="about_us"),
    path("contacts/", contacts, name='contacts'),
    path("test/", test, name="test"),
    path("feedback/", feedback, name="feedback"),
    path("blanks/", blanks, name="blanks")
]

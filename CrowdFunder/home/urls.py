from django.urls import path
from .views import index, contact, about, SearchView

urlpatterns = [
    path("", index, name="index"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("search", SearchView.as_view(), name="search"),
]

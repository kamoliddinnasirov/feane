from django.urls import path
from main.views import Index, Book, About, Menu

urlpatterns = [
    path("", Index.as_view()),
    path("about/", About.as_view()),
    path('book/', Book.as_view()),
    path("menu/", Menu.as_view())
]
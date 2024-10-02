from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class Book(TemplateView):
    template_name = 'book.html'


class Menu(TemplateView):
    template_name = 'menu.html'


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post
# Create your views here.

class HomeListView(ListView):
    model=Post
    template_name = 'index.html'

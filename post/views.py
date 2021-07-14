from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class HomeListView(ListView):
    model=Post
    template_name = 'index.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['image', 'item', 'seller', 'price']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

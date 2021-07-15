from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class HomeListView(ListView):
    model = Post
    template_name = 'index.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['item', 'image', 'categories', 'seller', 'price']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class TopsListView(ListView):
    model = Post
    template_name = 'categories/tops_list.html'
    context_object_name = 'all_tops_list'

class PantsListView(ListView):
    model = Post
    template_name = 'categories/pants_list.html'
    context_object_name = 'all_pants_list'

class ShoesListView(ListView):
    model = Post
    template_name = 'categories/shoes_list.html'
    context_object_name = 'all_shoes_list'
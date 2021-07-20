from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post, Review
# Create your views here.

class HomeListView(ListView):
    model = Post
    template_name = 'index.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['item', 'image', 'categories', 'price']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        TFLC = get_object_or_404(Post, id=self.kwargs['pk'])
        favorite = False
        if TFLC.favorite.filter(id=self.request.user.id).exists():
            favorite = True
        context["favorite"] = favorite
        return context

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

def FavoriteView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.favorite.filter(id=request.user.id).exists():
        post.favorite.remove(request.user)
    else:
        post.favorite.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

def FavoritePostList(request, **kwargs):
    user = request.user
    favorite_posts = user.favorite.all()
    context = {
        "favorite_posts" : favorite_posts,
    }
    return render(request, "post_favorite_list.html", context)

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ['post', 'review', 'author',]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

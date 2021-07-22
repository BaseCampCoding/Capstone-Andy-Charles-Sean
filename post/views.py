from django.http import request
from django.urls.base import reverse
from django.views.generic import ListView, CreateView,View
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from .forms import CheckoutForm
from .models import Post, Address, Review
from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.conf import settings



import stripe
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
    context_object_name = 'all_item_list'

class ItemListView(ListView):
    model = Post
    template_name = 'summary.html'
    context_object_name = 'all_item_list'


class SuccessView(TemplateView):
    template_name = 'success.html'


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form' : form 
        }
        stripe.api_key = settings.STRIPE_SECRET_KEY
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1JFmozHSf7eLd1MvcHrP9xCw',
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/'
    )
        context = {
            'session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            # order = Post.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('address')
                apartment_address = form.cleaned_data.get('address2')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                same_shipping_address = form.cleaned_data.get('same_shipping_address')
                save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = Address(   
                    user = self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country =country,
                    zip = zip,
                    address_type ='B'
                )
                billing_address.save()
                # order.billing_address = billing_address
                # order.save()


                return redirect('checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, 'you do not have an active order')
            return redirect("summary")

class PaymentView(View):
    def get(self, *args,**kwargs):
        return render(self.request, "payment.html")

    # context_object_name = 'all_tops_list'

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


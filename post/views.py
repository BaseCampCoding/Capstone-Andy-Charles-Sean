from django.conf import settings
from django.views.generic import ListView, CreateView
from django.shortcuts import render , redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Post, Review
from django.http.response import HttpResponseRedirect
import stripe
from django.views import View
from django.urls.base import reverse, reverse_lazy
from .forms import ReviewForm
from django.db.models import Q
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




# Create your views here.

class HomeListView(ListView):
    model = Post
    template_name = 'index.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['item', 'image', 'categories', 'gender', 'price', 'description',]

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
        cart = False
        if TFLC.favorite.filter(id=self.request.user.id).exists():
            favorite = True

        if TFLC.cart.filter(id=self.request.user.id).exists():
            cart = True

        context["favorite"] = favorite
        context["cart"] = cart
        context['related_items'] = Post.get_related_items(TFLC)
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

def SuccessView(request):
    user = request.user
    shopping_cart_list = user.cart.all()
    template = render_to_string('email_template.html', {'name':request.user.username})
    email = EmailMessage(
        'Thanks for shopping at Shelf Wear',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently=False
    email.send()

    total = 0
    shipping = 5
    tax = 0.07
    for i in shopping_cart_list:
        total += i.price
    tax_amount = float(total) * tax
    tax_amount = "{:.2f}".format(tax_amount)
    total_cost = float(total) + shipping + float(tax_amount)
    total_cost = "{:.2f}".format(total_cost)

    cart = request.user.cart
    shopping_cart = []
    for item in cart.all():
        cart.remove(item)
        shopping_cart.append(item)

    context = {
        "shopping_cart" : shopping_cart,
        "total_items" : len(shopping_cart),
        "total" : total,
        "tax_amount" : tax_amount,
        "total_cost" : total_cost,
    }
    return render(request, "success.html", context)

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
        user = request.user
        shopping_cart_list = user.cart.all()
        total = 0
        cart_items = [] 
        for i in shopping_cart_list:
            data = {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': round(i.price * 100),
                        'product_data': {
                            'name': i
                        },
                    },
                    'quantity': 1,
                    'tax_rates':['txr_1JKSJdHSf7eLd1Mviy8HlMka']
                }
            cart_items.append(data)
        total = 0
        shipping = 5
        tax = 0.07
        for i in shopping_cart_list:
            total += i.price
        tax_amount = float(total) * tax
        tax_amount = "{:.2f}".format(tax_amount)
        total_cost = float(total) + shipping + float(tax_amount)
        total_cost = "{:.2f}".format(total_cost)
        if cart_items == []:
            return render(request,"shopping_cart.html")
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.create(
            amount= 1099,
            currency='usd',
            payment_method_types=['card'],
            receipt_email='andyduarte58@gmail.com',
)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            shipping_rates=['shr_1JIwhDHSf7eLd1MvgAzNqkPr'],
            shipping_address_collection={
            'allowed_countries': ['US'],
            },
          
            line_items=cart_items,
            mode='payment',
            #testing coupon system
            allow_promotion_codes=True,
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/shopping_cart/'
        )


        context = {
            'session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
            "total" : total,
            "tax_amount" : tax_amount,
            "total_cost" : total_cost,
            "shopping_cart_list" : shopping_cart_list,
            "shopping_cart" : len(shopping_cart_list)
        }

        return render(request, "shopping_cart.html", context)


class PaymentView(View):
    def get(self, *args,**kwargs):
        return render(self.request, "payment.html")

class PantsListView(ListView):
    model = Post
    template_name = 'categories/pants_list.html'
    context_object_name = 'all_pants_list'
    context_object_name = 'all_item_list'


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

def CartView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.cart.filter(id=request.user.id).exists():
        post.cart.remove(request.user)
    else:
        post.cart.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


# Testing remove items from cart
def remove(request):
    product = Post.objects.get(id=request.GET.get('pk'))
    shopping_cart_list = request.user.cart.all()
    shopping_cart_list.remove(product)
    return redirect('shopping_cart')

#---------------------

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_new.html'
    #fields='__all__'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.request.resolver_match.kwargs['pk']
        return super().form_valid(form)

     
class MaleListView(ListView):
    model = Post
    template_name = 'Gender/male_list.html'

class FemaleListView(ListView):
    model = Post
    template_name = 'Gender/female_list.html'

class SearchListView(ListView):
    model = Post
    template_name = 'search.html'
    def get_queryset(self):
        q = self.request.GET.get('q')
        posts = Post.objects.filter(
            Q(item__icontains=q) |
            Q(description__icontains=q) |
            Q(seller__username__icontains=q) |
            Q(categories__icontains=q)
        )
        return posts
    
class FilterListView(ListView):
    model = Post
    template_name = 'filter.html'
    def get_queryset(self):
        gender = self.request.resolver_match.kwargs['gender']
        category = self.request.resolver_match.kwargs['category']
        posts = Post.objects.filter(gender=gender, categories=category)
        return posts

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['item', 'image', 'categories', 'gender', 'price', 'description',]

    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.seler = self.request.user
        return super().form_valid(form)
    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user
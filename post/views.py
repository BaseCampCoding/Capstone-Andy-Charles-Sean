from django.http import request
from django.urls.base import reverse
from django.views.generic import ListView, CreateView,View
from django.views.generic.detail import DetailView
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist



from django.shortcuts import render , redirect

from .forms import CheckoutForm




from .models import Post, Address
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

class ItemListView(ListView):
    model = Post
    template_name = 'categories/tops_list.html'
    context_object_name = 'all_item_list'

class ItemListView(ListView):
    model = Post
    template_name = 'summary.html'
    context_object_name = 'all_item_list'


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form' : form 
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            # order = Post.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
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
            messages.warning(self.request, "Failed checkout")
            return redirect('checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, 'you do not have an active order')
            return redirect("summary")

class PaymentView(View):
    def get(self, *args,**kwargs):
        return render(self.request, "payment.html")
        


        







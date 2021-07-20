from django.urls import path
from .views import HomeListView, PostCreateView, PostDetailView, ItemListView, CheckoutView, PaymentView



urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('', HomeListView.as_view(), name='home'),
    path('tops/', ItemListView.as_view(), name='tops_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('summary/',ItemListView.as_view(), name='summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view, name='payment')



    
   
]

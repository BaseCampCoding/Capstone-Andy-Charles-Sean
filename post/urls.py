from django.urls import path
from .views import (
    CartView, FavoritePostList, FavoriteView, HomeListView, PantsListView, 
    PostCreateView, PostDetailView, SearchListView, ShoesListView
    ,TopsListView, ReviewCreateView, PaymentView, 
    FemaleListView, MaleListView,  SuccessView, FilterListView, checkout, PostUpdateView, PostDeleteView,
    )


urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('', HomeListView.as_view(), name='home'),
    path('tops/', TopsListView.as_view(), name='tops_list'),
    path('pants/', PantsListView.as_view(), name='pants_list'),
    path('shoes/', ShoesListView.as_view(), name='shoes_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('shopping/<int:pk>/', CartView, name='shopping'),
    path('shopping_cart/', checkout, name='shopping_cart'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('favorite/<int:pk>/', FavoriteView, name="favorite_post"),
    path('favorite_post/', FavoritePostList, name="post_favorite_list"),
    path('post/<int:pk>/review', ReviewCreateView.as_view(), name='review_new'),
    path('success/', SuccessView.as_view(),name = 'success'),
    path('male/', MaleListView.as_view(), name='male_list'),
    path('female/', FemaleListView.as_view(), name='female_list'),
    path('search/', SearchListView.as_view(), name='search'),
    path('<gender>/<category>/', FilterListView.as_view(), name='filter'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete')
 
]


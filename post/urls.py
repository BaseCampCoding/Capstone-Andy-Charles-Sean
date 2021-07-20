from django.urls import path
from .views import HomeListView, PantsListView, PostCreateView, PostDetailView, ShoesListView, TopsListView, ReviewCreateView


urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('', HomeListView.as_view(), name='home'),
    path('tops/', TopsListView.as_view(), name='tops_list'),
    path('pants/', PantsListView.as_view(), name='pants_list'),
    path('shoes/', ShoesListView.as_view(), name='shoes_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review_new'),
]
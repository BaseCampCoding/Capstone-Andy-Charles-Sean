from django.urls import path
from .views import HomeListView, PostCreateView, PostDetailView, ItemListView


urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('', HomeListView.as_view(), name='home'),
    path('tops/', ItemListView.as_view(), name='tops_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   
]
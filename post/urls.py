from django.urls import path
from .views import HomeListView, PostCreateView, PostDetailView


urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('', HomeListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   
]
from django.urls import path
from .views import SignUpView, UserAccountDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/<int:pk>/', UserAccountDetailView.as_view(), name='user_account')
]
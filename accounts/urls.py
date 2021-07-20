from django.urls import path
from .views import SignUpView, UserAccountDetailView, UserAccountEdit, UserAccountSellingView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/<int:pk>/', UserAccountDetailView.as_view(), name='user_account'),
    path('user/<int:pk>/edit', UserAccountEdit.as_view(), name='user_account_edit'),
    path('account/<int:pk>/selling/', UserAccountSellingView.as_view(), name='items_selling')
]
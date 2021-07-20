from accounts.models import CustomUser
from post.models import Post
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserAccountDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_account.html'

class UserAccountSellingView(DetailView):
    model = get_user_model()
    template_name = 'items_selling.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cur_user_id = self.request.resolver_match.kwargs["pk"]
        context['item_posts'] = Post.objects.filter(seller__id=cur_user_id)
        return context

class UserAccountEdit(UpdateView):
    model = CustomUser
    template_name = 'user_account_edit.html'
    fields = ['username', 'first_name', 'last_name', 'roles']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('user_account', kwargs={'pk': self.object.pk})

    def test_func(self): 
        return self.get_object() == self.request.user
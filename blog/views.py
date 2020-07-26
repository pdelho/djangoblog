from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from blog.models import Post

class HomeView(ListView):
    template_name = 'home.html'
    model = Post
    
class PostView(DetailView):
    template_name = 'blog/post.html'
    def get_object(self):
        return Post.objects.get(id=self.kwargs.get('postId'))
    

class CreateUserView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(CreateUserView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
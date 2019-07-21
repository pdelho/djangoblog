from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts':posts})

def post(request, postId):
    post = Post.objects.get(id=postId)
    return render(request, "blog/post.html", {'post':post})

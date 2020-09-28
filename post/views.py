from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

# Create your views here.
# def registro(request):
#     return render(request, 'registro.html')

# def my_login(request):
#     return render(request, 'login.html')

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

@login_required
def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})
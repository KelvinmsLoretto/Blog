from django.shortcuts import render
from blog.models import Post
# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'posts': post})
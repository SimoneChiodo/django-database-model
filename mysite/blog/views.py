from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
  posts = Post.objects.all().order_by('-data_creazione')
  return render(request, "index.html", { "posts": posts })

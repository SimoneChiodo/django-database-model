from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
  posts = Post.objects.all().order_by('-data_creazione')
  return render(request, "index.html", { "posts": posts })

def postDetail(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  return render(request, "postDetail.html", {"post": post})

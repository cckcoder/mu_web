from django.shortcuts import render, HttpResponse
from .models import Post

def home(request):
    # Query all post
    all_post = Post.objects.all()
    return render(request, 'blog/home.html', {'all_posts': all_post})

def about(request):
    return render(request, 'blog/about.html')

def post_details(request, post_id):
    return HttpResponse(f"Post id: {post_id}")
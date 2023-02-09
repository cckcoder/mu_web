from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post
from .forms import ContactForm

def home(request):
    # Query all post
    search_post = request.GET.get('search')
    if search_post:
        all_post = Post.objects.filter(Q(title__icontains=search_post))
    else:
        all_post = Post.objects.all()

    return render(request, 'blog/home.html', {'all_posts': all_post})

def about(request):
    return render(request, 'blog/about.html')

def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ContactForm()

    return render(request, 'blog/forms.html', {'form': form})
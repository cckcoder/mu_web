from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q

from .models import Post
from .forms import ContactForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    # Query all post
    all_post = Post.objects.all()
    return render(request, 'blog/home.html', {'all_posts': all_post})

def about(request):
    return render(request, 'blog/about.html')

@login_required(login_url="/sign-in")
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/thanks")

    return render(request, 'blog/contact.html', {'form': form})
    
def thank_page(request):
    return render(request, 'blog/thanks.html')

def search(request):
    search_post = request.GET.get("q")

    if search_post:
        posts = Post.objects.filter(
            Q(title__icontains=search_post)
        )
        post_number = posts.count()

        return render(request, 'blog/search.html', {
            'posts': posts,
            'post_number': post_number
        })
    else:
        return redirect("/")

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, 'blog/sign_up.html', {'form': form})

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, 'blog/sign_in.html')

def sign_out(request):
    logout(request)
    return redirect('/sign-in')
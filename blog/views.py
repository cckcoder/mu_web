from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse("<h1>Hello HOME</h1>")
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
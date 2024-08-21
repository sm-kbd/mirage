import time

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post
from .forms import BlogCreationForm

def home(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            post_ = Post(title=request.POST["title"], body=request.POST["body"], author=request.user)
            post_.save()
            return redirect('/')
        else:
            return redirect("/login/")
    else:
        form = BlogCreationForm()
    context = {"posts": Post.objects.all(), "title": "Home", "form": form}
    return render(request, "home.html", context)


def post(request, id):
    post_ = Post.objects.filter(id=id).first()
    data = {"post": post_, "title": post_.title}
    return render(request, "post.html", data)


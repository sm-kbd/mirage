from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post


def user(request, id):
    user_ = User.objects.filter(id=id).first()
    posts = Post.objects.filter(author=User.objects.filter(id=id).first()).all()
    data = {"user": user_, "posts": posts, "title": f"{user_.username}'s posts"}
    return render(request, "user.html", data)

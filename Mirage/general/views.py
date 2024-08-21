from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import logout as django_logout


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get("username")
            messages.success(request, f"アカウント作成しました!")
            return redirect("/login/")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form, "title": "Register"})

def logout(request):
    django_logout(request)
    return redirect('/')

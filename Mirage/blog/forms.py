from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post


class BlogCreationForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"placeholder":"タイトル"}), label='')
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":"8"}), label='')

    class Meta:
        model = Post
        fields = ("title", "body")

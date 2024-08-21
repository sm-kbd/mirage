from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(forms.ModelForm):
    username = forms.RegexField(label="ハンドル", max_length=30, regex=r'^[\w.+-]+$', 
                                help_text="30文字いない。英文字、和文字、'.', '-', '+'のみ。")
    password1 = forms.CharField(label="パスワード", widget=forms.PasswordInput)
    password2 = forms.CharField(label="パスワード（確認）", widget=forms.PasswordInput,
                                help_text="確認のため、同上のものを入力ください。")

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("同じハンドルのアカウントがすでに存在します。")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("パスワードが一致しません。"))
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm, MyPasswordChangeForm # forms.pyで定義したユーザ認証画面用フォームをImport
from django.urls import reverse_lazy

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/logout.html'

class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'accounts/password_change_done.html'

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm # forms.pyで定義したユーザ認証画面用フォームをImport

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/logout.html'

#class LogoutView(LoginRequiredMixin, View):
#    """ログアウトページ"""
#    def get(self):
#        return render('accounts/logout.html')
#logout = LogoutView.as_view()
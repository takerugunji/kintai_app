from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login.html', views.Login.as_view(), name='login'),
    path('logout.html', views.Logout.as_view(), name='logout'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'), # pw変更ページ追加
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'), # pw変更完了ページ追加
]
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login.html', views.Login.as_view(), name='login'),
    path('logout.html', views.Logout.as_view(), name='logout')
]
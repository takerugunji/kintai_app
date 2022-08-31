from django.urls import path
from . import views # viewsを読み込む

app_name = 'kintaiapp' # 他の場所からアプリ名での呼び出しを可能に
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('list/', views.list, name='list'),
]
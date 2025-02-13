from django.urls import path

from pybo import views

urlpatterns = [
    path('', views.index),  # config/urls.py 파일에서 이미 매핑
]
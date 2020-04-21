from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('introduce/', views.introduce, name="introduce"),
]
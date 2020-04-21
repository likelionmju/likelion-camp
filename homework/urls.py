from django.urls import path
from . import views

urlpatterns = [
    path('homeworklist/', views.homeworklist, name = 'homeworklist'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.QnA, name = 'QnA'),
    path('answer/', views.refresh, name='refresh')
]
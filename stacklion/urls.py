from django.urls import path
from . import views

urlpatterns = [
    path('QnA/', views.QnA, name = 'QnA'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeworklist, name="homeworklist"),
    path('new/', views.new, name='new'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]
from django.urls import path

from hw import views

urlpatterns = [
    path('', views.main, name="main"),
    path('detail/<int:id>', views.detail, name='detail'),
    path('notice_new', views.noticenew, name='notice_new'),
]

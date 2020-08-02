from django.urls import path
from hwmanage import views
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('', views.main, name="main"),
    path('detail/<int:homework_id>', views.detail, name='manage_detail'),
]

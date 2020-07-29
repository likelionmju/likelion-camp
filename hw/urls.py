from django.urls import path
from hw import views
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('', views.main, name="main"),
    path('detail/<int:id>', views.detail, name='detail'),
    path('notice_new', views.noticenew, name='notice_new'),
    path('submit/<int:id>', views.submit, name="submit"),
]

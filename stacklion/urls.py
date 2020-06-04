from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

urlpatterns = [
    path('', views.QnA, name = 'QnA'),
    path('refresh/', views.refresh, name='refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
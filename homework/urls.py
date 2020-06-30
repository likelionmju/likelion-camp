from django.urls import path
from . import views
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('', views.homeworklist, name="homeworklist"),
    path('new/', views.homeworknew, name='homeworknew'),

    path('detail/<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
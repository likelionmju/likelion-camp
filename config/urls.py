
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import page.views
import page.urls
import account.views
import account.urls
import homework.views
import homework.urls
import stacklion.views
import stacklion.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('account/',include('account.urls')),
    path('homework/',include('homework.urls')),
    path('stacklion/', include('stacklion.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from format import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls'), name='common'),
    path('', include('app.urls'), name='app'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

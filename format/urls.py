from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from format import settings

urlpatterns = [
  path('admin/', admin.site.urls),
  path('common/', include('common.urls'), name='common'),
  path('', include('app.urls'), name='app'),
  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

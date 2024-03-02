from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('control-panel/', admin.site.urls),
    path('', include('apps.alura_space.urls')),
    path('', include('apps.users.urls')),
    path('', include('photography_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

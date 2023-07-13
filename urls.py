from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mascotitas.urls')),
    path('accounts/', include('django.contrib.auth.urls')), #activamos los usuarios de admin
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

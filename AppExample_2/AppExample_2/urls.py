from django.contrib import admin
from women.views import *
from django.urls import path, include

from django.conf.urls.static import static
from AppExample_2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

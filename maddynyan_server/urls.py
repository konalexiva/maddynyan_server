from django.conf.urls.static import static
from django.urls import path

from maddynyan_server import settings

urlpatterns = [

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
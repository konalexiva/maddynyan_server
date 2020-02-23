from django.conf.urls.static import static
from django.urls import path, include

from maddynyan_server import settings

urlpatterns = [
                  path('api/', include('quotes_app.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

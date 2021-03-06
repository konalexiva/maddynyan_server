from django.conf.urls.static import static
from django.urls import path, include

from maddynyan_server import settings
from django.contrib import admin

urlpatterns = [
                  path('django/admin/', admin.site.urls),
                  path('api/quotes', include('quotes_app.urls')),
                  path('', include('redirects_app.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

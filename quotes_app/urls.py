from django.conf.urls.static import static
from django.urls import path, include

from maddynyan_server import settings
from quotes_app import views

urlpatterns = [
                  path('', views.Quotes.as_view()),
                  path('/rand', views.RandQuote.as_view())

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

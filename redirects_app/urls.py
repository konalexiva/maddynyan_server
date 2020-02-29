from django.conf.urls.static import static
from django.urls import path, include, re_path

from maddynyan_server import settings
from redirects_app import views

urlpatterns = [
                  path('instagram', views.instagram_redirect),
                  path('public', views.vk_public_redirect),
                  path('twitch', views.twitch_redirect),
                  # path('api/statistics/twitch', views.TwitchStatistics.as_view()),
                  # path('api/statistics/instagram', views.InstaStatistics.as_view()),
                  path('api/statistics', views.Statistics.as_view()),
                  re_path(r'^', views.rat_mania)

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

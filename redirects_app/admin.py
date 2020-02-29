from django.contrib import admin

# Register your models here.
from redirects_app.models import InstagramStatisticsModel, TwitchStatisticsModel

admin.site.register(InstagramStatisticsModel)
admin.site.register(TwitchStatisticsModel)

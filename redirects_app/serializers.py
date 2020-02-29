from rest_framework import serializers

from quotes_app.models import QuoteModel
from redirects_app.models import InstagramStatisticsModel, TwitchStatisticsModel


class InstagramStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramStatisticsModel
        fields = ('id', 'created_dt', 'count', 'type')


class TwitchStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchStatisticsModel
        fields = ('id', 'created_dt', 'count', 'type')

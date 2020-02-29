from rest_framework import serializers

from quotes_app.models import QuoteModel


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteModel
        fields = ('id', 'text')

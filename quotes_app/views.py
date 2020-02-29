from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from quotes_app.repositories import QuoteRepository
from quotes_app.serializers import QuoteSerializer


class Quotes(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        quotes = QuoteRepository.get_quotes()
        return Response(QuoteSerializer(quotes, many=True).data, status=200)


class RandQuote(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        quote = QuoteRepository.get_rand_quote()
        return Response(QuoteSerializer(quote, many=False).data, status=200)

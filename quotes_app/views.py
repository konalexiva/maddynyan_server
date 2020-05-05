from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from quotes_app.repositories import QuotesRepository
from quotes_app.serializers import QuoteSerializer


class Quotes(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        quotes = QuotesRepository().get_random()
        return Response(QuoteSerializer(quotes, many=True).data, status=status.HTTP_200_OK)


class RandQuote(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        quote = QuotesRepository().get_all()
        return Response(QuoteSerializer(quote, many=False).data, status=status.HTTP_200_OK)

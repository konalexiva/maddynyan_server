from django.http import HttpResponse, request, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from redirects_app.repositories import StatisticsRepository
from redirects_app.serializers import InstagramStatSerializer, TwitchStatSerializer


def instagram_redirect(request):
    t = timezone.now()
    print('----------')
    print('Дрочить на Олю в инсту')
    print('----------')
    StatisticsRepository().get_or_create_insta()
    response = HttpResponse("", status=302)
    response['Location'] = "http://instagram.com/nyanmaddy"
    return response


def twitch_redirect(request):
    print('----------')
    print('Дрочить на Олю на твиче')
    print('----------')
    StatisticsRepository().get_or_create_twitch()
    response = HttpResponse("", status=302)
    response['Location'] = "http://twitch.tv/maddynyan"
    return response


def vk_public_redirect(request):
    print('----------')
    print('В паблос')
    print('----------')
    response = HttpResponse("", status=302)
    response['Location'] = "https://vk.com/maddynyanstream"
    return response


def rat_mania(request):
    print('----------')
    print('мимо')
    print('----------')
    response = HttpResponse("", status=302)
    response['Location'] = "http://ratmania.ru/"
    return response


class InstaStatistics(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        models = StatisticsRepository.get_insta_week_statistic()
        serializer = InstagramStatSerializer(models, many=True)
        return Response(serializer.data, status=200)


class TwitchStatistics(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        models = StatisticsRepository.get_twitch_week_statistic()
        serializer = TwitchStatSerializer(models, many=True)
        return Response(serializer.data, status=200)


class Statistics(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        insta_models = StatisticsRepository.get_insta_week_statistic()
        insta_serializer = InstagramStatSerializer(insta_models, many=True)

        twitch_models = StatisticsRepository.get_twitch_week_statistic()
        twitch_serializer = TwitchStatSerializer(twitch_models, many=True)

        return JsonResponse(data={'insta': insta_serializer.data, 'twitch': twitch_serializer.data},
                            status=200)


def index(request):
    return render(request, 'redirects_app/index.html')

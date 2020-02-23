from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


def instagram_redirect(request):
    print('----------')
    print('Дрочить на Олю в инсту')
    print('----------')
    response = HttpResponse("", status=302)
    response['Location'] = "http://instagram.com/nyanmaddy"
    return response


def twitch_redirect(request):
    print('----------')
    print('Дрочить на Олю на твиче')
    print('----------')
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
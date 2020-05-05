import datetime
import json
from json import JSONDecodeError

from backend.errors.errors import Errors
from backend.errors.http_exception import HttpException
from django.utils.timezone import make_aware
from djangorestframework_camel_case.util import underscoreize


def get_body_in_request(request):
    if not request.body:
        raise HttpException(detail=Errors.BAD_REQUEST.name, status_code=Errors.BAD_REQUEST)
    try:
        data = json.loads(request.body.decode('utf-8'))
        return underscoreize(data)
    except JSONDecodeError:
        data = request.POST
        return underscoreize(data)


def choices(em):
    return [(e.value, e.name) for e in em]


def milliseconds_to_datetime(milliseconds):
    """ Перевод из любого таймштампа в дату """
    # make_aware используется для учета временной зоны (учитывается в БД)
    overflowed_date = make_aware(datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=milliseconds))
    return overflowed_date


def datetime_to_milliseconds(date_time):
    try:
        # для возможности выбора дат за пределами границ таймштампа используем разницу дат с эпохой
        # replace(tzinfo=None) используется для удаления информации о временной зоне, чтобы получить разность
        diff = date_time.replace(tzinfo=None) - datetime.datetime(1970, 1, 1)
        large_timestamp = int(diff.total_seconds() * 1000)
        return large_timestamp
    except Exception as e:
        print(e)
        return None


def create_admin_serializer(cls):
    meta_model = cls.Meta.model

    class AdminSerializer(cls):
        class Meta:
            model = meta_model
            exclude = ['deleted']

    return AdminSerializer


def user_is_admin(user):
    return 'admins' in user.groups.values_list('name', flat=True)

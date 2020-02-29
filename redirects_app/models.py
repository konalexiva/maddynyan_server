from django.db import models

# Create your models here.
from django.utils import timezone

from redirects_app.enums import StatTypeEnum


class StatisticsModel(models.Model):
    created_dt = models.DateField(null=False, blank=False)
    count = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        abstract = True


class InstagramStatisticsModel(StatisticsModel):
    type = models.IntegerField(default=StatTypeEnum.INSTA.value)

    def __str__(self):
        return f'({self.created_dt})\t{self.count}'

    class Meta:
        verbose_name = 'Инстаграм'
        verbose_name_plural = 'Инстаграм'


class TwitchStatisticsModel(StatisticsModel):
    type = models.IntegerField(default=StatTypeEnum.TWITCH.value)

    def __str__(self):
        return f'({self.created_dt})\t{self.count}'

    class Meta:
        verbose_name = 'Твич'
        verbose_name_plural = 'Твич'

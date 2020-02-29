from django.db.models import Q
from django.utils import timezone

from redirects_app.models import InstagramStatisticsModel, TwitchStatisticsModel


class StatisticsRepository:

    @staticmethod
    def get_or_create_insta():
        date = timezone.now().date()
        #  year = date.year
        # month = date.month
        # day = date.day
        # date = datetime.date(year, month, day)

        model, created = InstagramStatisticsModel.objects.get_or_create(
            created_dt=timezone.now().date(),
            defaults={'created_dt': date, 'count': 0})
        model.count = model.count + 1
        model.save()

    @staticmethod
    def get_or_create_twitch():
        date = timezone.now().date()

        model, created = TwitchStatisticsModel.objects.get_or_create(
            created_dt=timezone.now().date(),
            defaults={'created_dt': date, 'count': 0})
        model.count = model.count + 1
        model.save()

    @staticmethod
    def get_insta_week_statistic():
        current_date = timezone.now()
        return InstagramStatisticsModel.objects.filter(
            Q(created_dt__gt=current_date - timezone.timedelta(weeks=1)) & Q(created_dt__lte=current_date)).all()


    @staticmethod
    def get_twitch_week_statistic():
        current_date = timezone.now()
        return TwitchStatisticsModel.objects.filter(
            Q(created_dt__gt=current_date - timezone.timedelta(weeks=1)) & Q(created_dt__lte=current_date)).all()

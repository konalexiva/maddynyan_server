from quotes_app.models import QuoteModel
from random import randint


class QuoteRepository:
    @staticmethod
    def get_quotes():
        return QuoteModel.objects.all()

    @staticmethod
    def get_rand_quote():
        quotes_list = QuoteModel.objects.all()
        index = randint(0, quotes_list.__len__() - 1)
        return quotes_list[index]

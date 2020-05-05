from backend.repositories import BaseRepository
from quotes_app.models import QuoteModel


class QuotesRepository(BaseRepository):
    def __init__(self):
        super().__init__(QuoteModel)

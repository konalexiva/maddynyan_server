from django.db import models

# Create your models here.
from backend.models import BaseModel


class QuoteModel(BaseModel):
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.id}\t{self.text}'

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

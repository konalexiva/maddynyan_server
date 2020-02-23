from django.db import models


# Create your models here.

class QuoteModel(models.Model):
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return '%d (%s)' % (self.id, self.text)

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

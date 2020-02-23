from django.contrib import admin

# Register your models here.
from quotes_app.models import QuoteModel

admin.site.register(QuoteModel)

__author__ = 'pushkar'

from django.contrib import admin
from rango.models import Company, StockPrice

# class TickerInline(admin.StackedInline):
#     model = Ticker

class StockPriceInline(admin.StackedInline):
    model = StockPrice
    extra = 1

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Details', {'fields':['name', 'ticker']}),
    ]

    inlines = [StockPriceInline]

admin.site.register(Company, CompanyAdmin)



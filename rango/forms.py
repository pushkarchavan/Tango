__author__ = 'pushkar'

from django import forms
from rango.models import Company, StockPrice

class CompanyForm (forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name of Company")
    ticker = forms.CharField(max_length=5,help_text="Company's Ticker")

    class Meta:
        model = Company

class StockPriceForm(forms.ModelForm):
    price = forms.DecimalField(max_digits=6, decimal_places=2, help_text="0000.00")

    class Meta:
        model = StockPrice


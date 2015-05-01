__author__ = 'pushkar'

from django import forms
from rango.models import Company, StockPrice

class CompanyForm (forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name of Company")
    ticker = forms.CharField(max_length=5,help_text="Company's Ticker")

    class Meta:
        model = Company


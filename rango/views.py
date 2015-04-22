# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Company, StockPrice

def index(request):
    context = RequestContext(request)

    company_list = Company.objects.order_by('name') #TODO Sort by currentPrice

    context_dict = {'companies':company_list}

    for company in company_list:
        company.url = company.ticker.lower()

    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)

    context_dict = {'aboutRango' : 'Some text here'}

    return render_to_response('rango/about.html', context_dict, context)

def company(request, company_ticker_url):
    context = RequestContext(request)

    # Getting Company Ticker from the URL
    company_ticker = company_ticker_url.upper()
    context_dict = {'ticker':company_ticker}

    # Get Company Details and prices for specific company
    # If company does not exist, show an error page
    try:
        company= Company.objects.get(ticker=company_ticker)
        context_dict['company'] = company
        prices = StockPrice.objects.filter(tickr=company)
        context_dict['prices'] = prices

    except Company.DoesNotExist:
        pass

    return render_to_response('rango/company.html', context_dict, context)

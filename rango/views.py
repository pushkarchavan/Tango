# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Company, StockPrice

def index(request):
    context = RequestContext(request)

    company_list = Company.objects.order_by('name')

    context_dict = {'companies':company_list}

    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)

    context_dict = {'aboutRango' : 'Some text here'}

    return render_to_response('rango/about.html', context_dict, context)


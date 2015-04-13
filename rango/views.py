# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)

    context_dict = {'boldmessage' : 'Coming Soon !!!'}

    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)

    context_dict = {'aboutRango' : 'Some text here'}

    return render_to_response('rango/about.html', context_dict, context)

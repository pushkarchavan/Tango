__author__ = 'pushkar'

import os


def populate():
    company_goog = add_company('General Motors Company', 'GM')

    add_price(tickr=company_goog, time=timezone.now(), price=101.00)


    company_appl = add_company("Tesla Motors, Inc", 'TSLA')

    add_price(tickr=company_appl,time=timezone.now(), price=120.00)

    #TODO Analyze the commented code below for print statements
    # Print out what we have added to the user.
    # for c in Company.objects.all():
    #     for p in StockPrice.objects.filter(tickr=c):
    #         print "- {0} - {1}".format(str(c), str(p))

def add_price(tickr,time,price):
    p = StockPrice.objects.get_or_create(tickr=tickr, time=time, price=price)[0]
    return p

def add_company(name, ticker):
    c = Company.objects.get_or_create(name=name, ticker=ticker)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tango.settings')
    from rango.models import Company, StockPrice
    from django.utils import timezone
    populate()

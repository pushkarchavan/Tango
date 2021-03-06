from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ticker = models.CharField(max_length=5, unique=True)

    class Meta:
        verbose_name_plural = "Companies"

    def currentPrice(self):
        # Check if there are any recorded prices for a company
        # If Prices are found, return the latest price or return
        if self.stockprice_set.count():
            b = self.stockprice_set.order_by('-pk')[0]
            current_price = b.price
        else:
            current_price = 0
        return current_price

    def __unicode__(self):
        return self.name


class StockPrice(models.Model):
    tickr = models.ForeignKey(Company)
    time = models.DateTimeField('Date/Time') #TODO Possible improvement of date format
    price = models.DecimalField(max_digits=6, decimal_places=2)

    #TODO fix the toString method to reflect accurate data
    # def __unicode__(self):
    #     c = Company.objects.get(name = self.tickr.__str__())
    #     return c.ticker

    def __unicode__(self):
        return self.price.__str__()


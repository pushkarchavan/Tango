from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ticker = models.CharField(max_length=5, unique=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __unicode__(self):
        return self.name


class StockPrice(models.Model):
    tickr = models.ForeignKey(Company)
    time = models.DateTimeField('Date/Time') #TODO Possible improvement of date format
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.tickr

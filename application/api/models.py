from django.db import models
from decimal import Decimal


class Store(models.Model):
    name = models.TextField(max_length=30, unique=True)
    address = models.TextField(max_length=30)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    description = models.TextField(max_length=500)
    store = models.ForeignKey(Store, related_name='articles')
    total_in_shelf = models.IntegerField(default=0)
    total_in_vault = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
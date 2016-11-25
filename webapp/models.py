from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=70)
    vat_payer = models.BooleanField()  # Check syntax
    vat_number = models.CharField(max_length=20)
    reg_number = models.CharField(max_length=20)
    comment = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return self.name

class InvoiceCustomer(models.Model):
    number = models.CharField(max_length=30)
    amount_total = models.IntegerField()
    comment = models.TextField()

    def __unicode__(self):
        return self.number

class Product(models.Model):
    types = [
        ('product', 'Product'),
        ('service', 'Service')
    ]

    name = models.CharField(max_length=70)
    number = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=types, default='product')

    def __unicode__(self):
        return "[%s] %s" % (self.number, self.name)

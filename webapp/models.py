from __future__ import unicode_literals

from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=70)
    vat_payer = models.BooleanField()
    vat_number = models.CharField(blank=True, max_length=20)
    reg_number = models.CharField(blank=True, max_length=20)
    comment = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    customer = models.BooleanField(default=True)
    supplier = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)


class Company(Partner):
    employee_count = models.IntegerField(default=1)


class Invoice(models.Model):
    types = [
        ('customer', 'Customer'),
        ('supplier', 'Supplier')
    ]

    number = models.CharField(max_length=30)
    amount_total = models.IntegerField()
    comment = models.TextField()
    type = models.CharField(max_length=20, choices=types, default='customer')
    partner_id = models.ForeignKey('Partner', default=1, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.number

class InvoiceLine(models.Model):
    quantity = models.IntegerField()
    amount = models.FloatField()
    description = models.CharField(max_length=40)
    invoice_id = models.ForeignKey('Invoice', default=1, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', blank=True, default=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s %s X %s" % (self.product_id.name or None, self.description, self.quantity)

class Product(models.Model):
    types = [
        ('product', 'Product'),
        ('service', 'Service')
    ]

    name = models.CharField(max_length=70)
    internal_reference = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=types, default='product')

    def __unicode__(self):
        return "[%s] %s" % (self.internal_reference, self.name)

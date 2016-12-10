from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# DEFAULTS
def get_default_invoice_comment():
    return "Enter comment here..."

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
    date_invoice = models.DateTimeField('Date', default=timezone.now())
    comment = models.TextField(default=get_default_invoice_comment())
    type = models.CharField(max_length=20, choices=types, default='customer')
    partner_id = models.ForeignKey(
        'Partner', default=1, on_delete=models.CASCADE)
    currency_id = models.ForeignKey(
        'Currency', default=1, on_delete=models.CASCADE)

    @property
    def subtotal(self):
        total = 0.0
        for line in self.invoiceline_set.all():
            total += line.amount
        return total

    def __unicode__(self):
        return self.number

class InvoiceLine(models.Model):
    quantity = models.IntegerField(default=1)
    amount = models.FloatField()
    description = models.CharField(max_length=40)
    invoice_id = models.ForeignKey(
        'Invoice', default=1, on_delete=models.CASCADE)
    product_id = models.ForeignKey(
        'Product', blank=True, default=False, on_delete=models.CASCADE)

    @property
    def unit_price(self):
        if self.product_id:
            return self.product_id.unit_price
        else:
            return 0.0

    @property
    def subtotal(self):
        return self.unit_price * self.quantity

    def __unicode__(self):
        return "%s %s X %s" % (
            self.product_id.name or None, self.description, self.quantity)

class Product(models.Model):
    types = [
        ('product', 'Product'),
        ('service', 'Service')
    ]

    name = models.CharField(max_length=70)
    internal_reference = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=types, default='product')
    unit_price = models.FloatField(default=0.0)

    def __unicode__(self):
        return "[%s] %s" % (self.internal_reference, self.name)

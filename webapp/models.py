from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# DEFAULTS


def get_default_invoice_comment():
    return "Enter comment here..."


# TODO: figure out a way to do this, since can only put default get here, but
# can't call Tax class before it's definition
# def get_default_tax():
#     try:
#         return Tax.objects.get(name='None')
#     except Tax.DoesNotExist:
#         return False


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


class Address(models.Model):
    types = [
        ('contact', 'Contact'),
        ('invoice', 'Invoice'),
        ('shipping', 'Shipping'),
    ]
    partner_id = models.ForeignKey('Partner', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type = models.CharField('Address Type', max_length=10, choices=types)
    street = models.CharField('Street', blank=True, max_length=40)
    city = models.CharField('City', blank=True, max_length=30)
    zip = models.CharField('Zip', blank=True, max_length=15)
    country = models.CharField('Country', blank=True, max_length=30)
    phone = models.CharField('Phone', blank=True, max_length=20)
    fax = models.CharField('Fax', blank=True, max_length=20)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return "%s [%s] %s" % (
             self.partner_id.name or None, self.type or None, self.name or None)


class Currency(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)

    def __unicode__(self):
        return self.code


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
    def tax_amount(self):
        """Return total tax amount."""
        total = 0
        for line in self.invoiceline_set.all():
            total += line.tax_amount
        return total

    @property
    def subtotal(self):
        """Return invoice total (without tax)."""
        total = 0.0
        for line in self.invoiceline_set.all():
            total += line.subtotal
        return total

    @property
    def total(self):
        return self.subtotal + self.tax_amount

    def __unicode__(self):
        return self.number


class InvoiceLine(models.Model):
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=40, blank=True, null=True)
    invoice_id = models.ForeignKey(
        'Invoice', default=1, on_delete=models.CASCADE)
    product_id = models.ForeignKey(
        'Product', default=False, on_delete=models.CASCADE)
    tax_id = models.ForeignKey(
        'Tax', blank=True, null=True, on_delete=models.CASCADE)

    @property
    def unit_price(self):
        if self.product_id:
            return self.product_id.unit_price
        else:
            return 0.0

    @property
    def subtotal(self):
        return self.unit_price * self.quantity

    @property
    def tax_amount(self):
        tax = self.tax_id
        if tax:
            if tax.type == 'percent':
                return self.subtotal * tax.rate
            elif tax.type == 'flat':
                return tax.rate
        else:
            return 0.0

    def __unicode__(self):
        return "%s %s X %s" % (
            self.product_id.name or None, self.description, self.quantity)


class Product(models.Model):
    """Product model."""
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


class Tax(models.Model):
    """Tax model that allows creating and later applying various taxes."""
    types = [
        ('flat', 'Flat Rate'),
        ('percent', 'Percentage')
    ]

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=types, default='percent')
    code = models.CharField(max_length=3)
    rate = models.FloatField(default=0.0)

    def __unicode__(self):
        return "[%s] %s" % (self.code, self.name)
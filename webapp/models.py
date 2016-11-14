from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=70)
    vat_payer = models.BooleanField()  # Check syntax
    vat_number = models.CharField(max_length=20)
    reg_number = models.CharField(max_length=20)


class InvoiceCustomer(models.Model):
    number = models.CharField(max_length=30)


class Product(models.Model):
    number = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

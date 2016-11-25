from django.contrib import admin
from webapp.models import Customer, InvoiceCustomer
# Register your models here.

admin.site.register(Customer)
admin.site.register(InvoiceCustomer)
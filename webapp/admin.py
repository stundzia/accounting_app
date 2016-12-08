from django.contrib import admin
from webapp.models import Customer, InvoiceCustomer, InvoiceLine, Product
# Register your models here.

admin.site.register(Customer)
admin.site.register(InvoiceCustomer)
admin.site.register(InvoiceLine)
admin.site.register(Product)

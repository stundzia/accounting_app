from django.contrib import admin
from .models import Partner, Invoice, InvoiceLine, Product, Tax, Currency, Address, Company
# Register your models here.

admin.site.register(Partner)
admin.site.register(Invoice)
admin.site.register(InvoiceLine)
admin.site.register(Product)
admin.site.register(Tax)
admin.site.register(Currency)
admin.site.register(Address)
admin.site.register(Company)

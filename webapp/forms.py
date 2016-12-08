from django import forms
from django.forms import ModelForm
from webapp.models import InvoiceCustomer, Product, Customer

class InvoiceCustomerForm(ModelForm):
    created_at = forms.DateTimeField()

    class Meta:
        model = InvoiceCustomer
        fields = ['number', 'customer_id', 'comment']

class Customer(ModelForm):
    created_at = forms.DateTimeField()

    class Meta:
        model = Customer
        fields = ['name', 'vat_payer', 'vat_number', 'reg_number']
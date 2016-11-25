from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from webapp.models import Customer, InvoiceCustomer
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^customers/list$',
        ListView.as_view(
            queryset=Customer.objects.all().order_by("name")[:50],
            template_name="webapp/customers_list.html"
        )
    ),
    url(
        r'^invoices/list$',
        ListView.as_view(
            queryset=InvoiceCustomer.objects.all().order_by("number")[:50],
            template_name="webapp/invoice_list.html"
        )
    ),
    url(
        r'^invoices/(?P<pk>\d+)$',
        DetailView.as_view(
            model=InvoiceCustomer,
            template_name="webapp/invoice.html")
    ),
    url(
        r'^customers/(?P<pk>\d+)$',
        DetailView.as_view(
            model=Customer,
            template_name="webapp/customer.html")
    ),
]

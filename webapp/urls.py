from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from django.forms import ModelForm
from webapp.models import Partner, Invoice, Product, InvoiceLine
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^invoices_form/(?P<pk>\d+)$',
        views.InvoiceCreateForm.as_view(),
        name='invoice_create_form'),
    url(
        r'^customers/list$',
        ListView.as_view(
            queryset=Partner.objects.filter(customer=True).order_by("name")[:50],
            template_name="webapp/partner_list.html"
        ), name='customer_list'
    ),
    url(
        r'^suppliers/list$',
        ListView.as_view(
            queryset=Partner.objects.filter(supplier=True).order_by("name")[
                     :50],
            template_name="webapp/partner_list.html"
        ), name='supplier_list'
    ),
    url(
        r'^invoices/list$',
        ListView.as_view(
            queryset=Invoice.objects.all().order_by("number")[:50],
            template_name="webapp/invoice_list.html"
        ), name='invoice_list'
    ),
    url(
        r'^invoices/(?P<pk>\d+)$',
        DetailView.as_view(
            model=Invoice,
            template_name="webapp/invoice.html"
        ), name='invoice_detail'
    ),
    url(
        r'^partners/(?P<pk>\d+)$',
        DetailView.as_view(
            model=Partner,
            template_name="webapp/partner.html"
        ), name='partner_detail'
    ),
    url(
        r'^products/list$',
        ListView.as_view(
            queryset=Product.objects.all().order_by("internal_reference")[:50],
            template_name="webapp/products.html"
        ), name='product_list'
    ),
    url(
        r'^products/(?P<pk>\d+)$',
        DetailView.as_view(
            model=Product,
            template_name="webapp/product.html"
        ), name='product_detail'
    ),
]

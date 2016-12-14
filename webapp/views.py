from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse, request, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from .forms import InvoiceForm, InvoiceLineFormSet
from django.views import generic
from .models import Invoice, Partner, Product


def index(request):
    latest_invoices = Invoice.objects.order_by('-date_invoice')[:10]
    context = {
        'invoices': latest_invoices,
    }
    return render(request, 'webapp/home.html', context)


def submit_invoice(request):
    if request.POST:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoiceline_formset = InvoiceLineFormSet(request.POST, instance=invoice)
            if invoiceline_formset.is_valid():
                invoice.save()
                invoiceline_formset.save()
                return HttpResponseRedirect(reverse('invoice_list'))
    else:
        form = InvoiceForm()
        invoiceline_formset = InvoiceLineFormSet(instance=Invoice())
    return render_to_response("webapp/invoice_submit.html", {
        "form": form,
        "invoiceline_formset": invoiceline_formset,
    },
                              # context_instance=RequestContext(request)
                              # TODO: ^unexpected kwarg
                              )

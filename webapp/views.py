from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import RequestContext
from .forms import InvoiceForm
from django.views import generic
from .models import Invoice, Partner, Product

def index(request):
    latest_invoices = Invoice.objects.order_by('-date_invoice')[:10]
    context = {
        'invoices': latest_invoices,
    }
    return render(request, 'webapp/home.html', context)

# def suppliers(request):
#     suppliers = get_list_or_404(Partner, supplier=True)
#     return render(request, 'webapp/partner_list.html', {'suppliers': suppliers})

# def invoice_create(request, pk):
#     form = InvoiceForm()
#     return render_to_response('invoice_create_form.html',
#                               {'form': InvoiceForm, },
#                               context_instance=RequestContext(request),
#             )

class InvoiceCreateForm(generic.FormView):
    form_class = InvoiceForm
    template_name = 'webapp/invoice_create_form.html'


def customers(request):
    recs = [
        {
            'name': 'John',
            'id': 1,
        },
        {
            'name': 'Tom',
            'id': 2,
        }
    ]
    vals = {
        'thead': 'Customers',
        'tfoot': 'Table Footer',
        'recs': recs,
    }
    return render(request, 'webapp/customers.html', vals)

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from webapp.forms import InvoiceForm

def index(request):
    # return HttpResponse("<h1>Welcome!</h1>")
    return render(request, 'webapp/home.html')

def invoice_create(request):
    form = InvoiceForm()
    return render_to_response('invoice_create_form.html',
                              {'form': form, },
                              context_instance=RequestContext(request),
            )

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

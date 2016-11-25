from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>Welcome!</h1>")
    return render(request, 'webapp/home.html')

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

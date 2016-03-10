from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from plans.models import Plans
from client.models import Client
from invoice.models import Invoice
from connections.models import Connection
#from enquiries.models import Enquiries


def client(request):
    plans = Plans.objects.all()
    return render(
        request,
        'base.html',
        {'plans': plans}
    )

def dashboard(request):
    context = {}
    clients = Client.objects.all().count()
    invoices = Invoice.objects.all().count()
    latest_invoice = Invoice.objects.all().order_by('id')[:7]
    connections = Connection.objects.all().count()
    #enquiries = Enquiries.objects.all().count()

    context['client'] = clients
    context['invoice'] = invoices
    context['connection'] = connections
    context['enquiry'] = 0
    context['latest_invoice'] = latest_invoice
    return render(
        request,
        'core/dashboard.html',
        context
    )

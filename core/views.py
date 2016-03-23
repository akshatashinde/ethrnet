from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from plans.models import Plans
from client.models import Client
from invoice.models import Invoice
from connections.models import Connection
from client.forms import ClientFormMin, AddressForm
from fileupload.forms import PictureForm
#from enquiries.models import Enquiries


def client(request):
    context = {}
    plans = Plans.objects.all()

    client_form = ClientFormMin()
    address_form = AddressForm()

    pic1 = PictureForm()
    pic2 = PictureForm()

    context['client_form'] = client_form
    context['address_form'] = address_form
    context['plans'] = plans
    context['pic1'] = pic1
    context['pic2'] = pic2
    return render(
        request,
        'base.html',
        context
    )

def dashboard(request):
    context = {}
    clients = Client.objects.all(request.user).count()
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

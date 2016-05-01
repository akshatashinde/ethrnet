import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from account.models import Branch
from plans.models import Plans
from client.models import Client
from invoice.models import Invoice
from connections.models import Connection
from client.forms import ClientFormMin, AddressForm
from fileupload.forms import PictureForm
#from enquiries.models import Enquiries
from django.contrib.auth.decorators import login_required
from connections.forms import ConnectPlanForm


def client(request):
    context = {}
    plans = Plans.objects.all(request.user)

    client_form = ClientFormMin()
    address_form = AddressForm()
    plan_form = ConnectPlanForm()

    pic1 = PictureForm()
    pic2 = PictureForm()

    context['client_form'] = client_form
    context['address_form'] = address_form
    context['plan_form'] = plan_form
    context['plans'] = plans
    context['pic1'] = pic1
    context['pic2'] = pic2
    return render(
        request,
        'base.html',
        context
    )


@login_required
def dashboard(request):
    context = {}
    clients = Client.objects.all(request.user).count()
    invoices = Invoice.objects.all(request.user).count()
    latest_invoice = Invoice.objects.all(request.user).order_by('id')[:7]
    connections = Connection.objects.all(request.user).count()
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


import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

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
    if request.method == "POST":
        client_form = ClientFormMin(request.POST)
        address_form = AddressForm(request.POST)
        plan_form = ConnectPlanForm(request.POST)

        if (client_form.is_valid() and address_form.is_valid()
        and plan_form.is_valid()):
            client = client_form.save()
            address = address_form.save()
            conn_plan = plan_form.save(commit=False)

            client.Address = address
            client.save()

            conn_plan.client = client
            conn_plan.branch = address.area
            conn_plan.save()

            context['client_success'] = True
            context['client_no_error'] = True

            client_form = ClientFormMin()
            address_form = AddressForm()
            plan_form = ConnectPlanForm()

            pic1 = PictureForm()
            pic2 = PictureForm()
        else:
            context['client_success'] = True
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

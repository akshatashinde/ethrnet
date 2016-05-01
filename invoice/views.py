import json

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from invoice.forms import InvoiceForm, InvoiceIteamForm
from invoice.models import Invoice, InvoiceItem, Currency
from invoice.pdf import draw_pdf
from invoice.utils import pdf_response
from client.models import Client
from account.models import UserAddress
from django.template import RequestContext
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.functional import curry
from django.views.decorators.http import require_http_methods
from inventory.models import IteamVariation
from plans.models import Plans


def pdf_view(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)


@login_required
def pdf_user_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id, user=request.user)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)


def get_invoice(request, id):
    invoice = Invoice.objects.filter(id=id)
    if invoice:
        invoice = invoice[0]
        client = Client.objects.get(id=invoice.user.id)
        address = UserAddress.objects.get(id=invoice.address.id)
        invoice_items = InvoiceItem.objects.filter(invoice=invoice.id)
        return render(
            request,
            'invoice/invoice.html',
            {'invoice': invoice,
             'client': client,
             'address': address,
             'invoice_items': invoice_items
             })
    return HttpResponseRedirect(reverse('ethernet-invoice:create_invoice'))


def create_invoice(request):
    flag = False
    msg = ""
    invoiceIteamFactory = formset_factory(InvoiceIteamForm, extra=3, can_delete=True)
    # invoiceIteamFactory.form = staticmethod(curry(InvoiceIteamForm, user=request.user))
    if request.method == "POST":
        data = request.POST
        client = Client.objects.filter(client_id__iexact=data['user'])
        if client:
            invoice = Invoice(
                user=client[0],
                invoice_date=data['invoice_date'],
                paid_date=data['paid_date'],
            )
            if data.get('draft'):
                invoice.draft = True
            else:
                invoice.draft = False
            invoice.address = invoice.user.Address
            invoice.currency = Currency.objects.all()[0]
            invoice.save()
            invoice.invoice_id = 'EN0000' + str(invoice.id)
            print invoice.id
            if not request.user.is_staff:
                invoice.branch = request.user.userprofile.branch
            invoice.save()

            formset = invoiceIteamFactory(request.POST)
            count = 0
            for form in formset:
                count += 1
            for i in range(0, count):
                name = 'form-' + str(i) + '-item'
                itemvariation = IteamVariation.objects.filter(code__iexact=data[name])
                plans = Plans.objects.filter(code__iexact=data[name])
                description = ""
                quantity = 0
                unit_price = 0

                if itemvariation:
                    itemvariation = itemvariation[0]
                else:
                    itemvariation = None

                if plans:
                    plans = plans[0]
                else:
                    plans = None

                if data.get('form-' + str(i) + '-description'):
                    description = data.get('form-' + str(i) + '-description')

                if data.get('form-' + str(i) + '-quantity'):
                    quantity = data.get('form-' + str(i) + '-quantity')

                if data.get('form-' + str(i) + '-unit_price'):
                    unit_price = data.get('form-' + str(i) + '-unit_price')

                invoice_item = InvoiceItem(
                    item=itemvariation,
                    plan=plans,
                    description=description,
                    unit_price=unit_price,
                    quantity=quantity
                )
                invoice_item.invoice = invoice
                invoice_item.save()

                msg = "Invoice added Successfully."
            return HttpResponseRedirect(reverse('ethernet-invoice:get_invoice',
                                                    args=(invoice.id,)))
    form = InvoiceForm()
    formset = invoiceIteamFactory()
    return render(
        request,
        'invoice/new_invoice.html',
        {
            'form': form,
            'formset': formset,
            'page': 'invoice',
            'flag': flag,
            'msg': msg
        },
        context_instance=RequestContext(request),
    )


def invoice_list(request):
    invoices = Invoice.objects.all(request.user)
    return render(
        request,
        'invoice/invoice_list.html',
        {
            'invoices': invoices,
            'page': 'invoice'
        })


def invoice_send(request, id):
    invoice = Invoice.objects.filter(id=id)
    if invoice:
        invoice = invoice[0]
        invoice.send_invoice()
        return HttpResponse('success')
    return HttpResponseRedirect(reverse('ethernet-invoice:create_invoice'))


@require_http_methods(["GET", "POST"])
def itemvarition_list(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        if request.user.is_staff:
            itemvariations = IteamVariation.objects.filter(code__icontains=q)
        else:
            itemvariations = IteamVariation.objects.filter(code__icontains=q, branch=request.user.userprofile.branch)
        results = []
        for itemvariation in itemvariations:
            results.append({
                'id': itemvariation.id,
                'label': itemvariation.code,
                'value': itemvariation.code,
            })

        if request.user.is_staff:
            itemvariations = Plans.objects.filter(code__icontains=q)
        else:
            itemvariations = Plans.objects.filter(code__icontains=q, branch=request.user.userprofile.branch)

        for itemvariation in itemvariations:
            results.append({
                'id': itemvariation.id,
                'label': itemvariation.code,
                'value': itemvariation.code,
            })

        data = json.dumps(results)
    else:
        data = 'Not valid request'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@require_http_methods(["GET", "POST"])
def get_price(request):
    mimetype = 'application/json'
    price = 0
    if request.is_ajax():
        data = request.POST
        if data.get('item'):

            itemvariation = IteamVariation.objects.filter(code__iexact=data['item'])
            if itemvariation:
                price = itemvariation[0].sale_price
                data = json.dumps(price)
                return HttpResponse(data, mimetype)
            plans = Plans.objects.filter(code__iexact=data['item'])
            if plans:
                price = plans[0].price

        data = json.dumps(price)
        return HttpResponse(data, mimetype)


@require_http_methods(["GET", "POST"])
def client_list(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        if request.user.is_staff:
            clients = Client.objects.filter(client_id__icontains=q)
        else:
            clients = Client.objects.filter(client_id__icontains=q, branch=request.user.userprofile.branch)
        results = []
        for client in clients:
            results.append({
                'id': client.id,
                'label': client.client_id,
                'value': client.client_id,
            })

        data = json.dumps(results)
    else:
        data = 'Not valid request'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

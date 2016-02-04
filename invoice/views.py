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


def pdf_view(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)


@login_required
def pdf_user_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id, user=request.user)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)


def get_invoice(request, id):
    invoice = get_object_or_404(Invoice, id=id)
    client = Client.objects.get(id=invoice.user.id)
    address = UserAddress.objects.get(id=invoice.address.id)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice.id)
    return render(
        request,
        'invoice/invoice.html',
        { 'invoice': invoice,
          'client': client,
          'address': address,
          'invoice_items': invoice_items
        })


def create_invoice(request):
    flag = False
    msg = ""
    invoiceIteamFactory = formset_factory(InvoiceIteamForm, extra=3, can_delete=True)
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        formset = invoiceIteamFactory(request.POST)
        if form.is_valid() and formset.is_valid():
            invoice = form.save(commit=False)
            invoice.address = invoice.user.Address
            invoice.currency = Currency.objects.all()[0]
            invoice.save()
            invoice.invoice_id = 'EN0000' + str(invoice.id)
            print invoice.id
            invoice.save()
            for form in formset:
                invoice_iteam = form.save(commit=False)
                invoice_iteam.invoice = invoice
                invoice_iteam.save()
                flag = True
                msg = "Invoice added Successfully."
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
    invoices = Invoice.objects.all()
    return render(
        request,
        'invoice/invoice_list.html',
        {
            'invoices': invoices,
            'page': 'invoice'
        })


def invoice_send(request, id):
    invoice = get_object_or_404(Invoice, id=id)
    invoice.send_invoice()
    return HttpResponse('success')
from django import forms
from invoice.models import Invoice, InvoiceItem


class InvoiceAdminForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude = []


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('user', 'invoice_date', 'paid_date', 'draft')


class InvoiceIteamForm(forms.ModelForm):

    class Meta:
        model = InvoiceItem
        fields = ('description', 'quantity', 'unit_price')

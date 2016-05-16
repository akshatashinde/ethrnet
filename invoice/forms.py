from django import forms

from client.models import Client
from invoice.models import Invoice, InvoiceItem
from inventory.models import  IteamVariation
from dal import autocomplete


class InvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Invoice
        exclude = []


class InvoiceForm(forms.ModelForm):
    user = forms.CharField()
    class Meta:
        model = Invoice
        fields = ('user', 'invoice_date', 'paid_date', 'draft')


class InvoiceIteamForm(forms.ModelForm):

    item = forms.CharField(widget=forms.TextInput(attrs={'class':'items'}))
    unit_price = forms.CharField(widget=forms.TextInput(attrs={'class':'prices', 'type':'number'}))

    class Meta:
        model = InvoiceItem
        fields = ('item', 'description', 'quantity', 'unit_price')

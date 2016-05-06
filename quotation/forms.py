from django import forms
from quotation.models import Quotation,Item


class QuotationForm(forms.ModelForm):
	class Meta:
		model = Quotation
		fields = ['client','quotation_no']

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields =['item','quantity','price']						
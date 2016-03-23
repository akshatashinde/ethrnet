from django import forms
from inventory.models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'


class IteamVariationForm(forms.ModelForm):
    class Meta:
        model = IteamVariation
        fields = ['price', 'sale_price', 'quantity', 'model_no', 'serial_no', 'warrenty_period', 'supplier',
                  'purchased_at', 'delivered_at', 'supplier']

from django import forms
from client.models import Client
from account.models import UserAddress


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["client_id", "name", "email", "phone_number"]


class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ["address", "flat_no", "society", "area", "city", "state", "country", "zipcode"]

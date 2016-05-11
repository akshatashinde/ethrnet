from django import forms
from client.models import Client
from account.models import UserAddress


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["client_id", "name", "email", "phone_number", "birth_date", "gender", "id_proof_types",
                  "address_proof_types"]


class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ["flat_no", "society", "area", "city", "state", "country", "zipcode"]

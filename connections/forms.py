from django import forms
from .models import Connection




class ConnectForm(forms.ModelForm):
    class Meta:
        model = Connection
        exclude = []

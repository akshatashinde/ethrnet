from django import forms
from .models import Connection


class ConnectForm(forms.ModelForm):

    class Meta:
        model = Connection
        exclude = []


class ConnectPlanForm(forms.ModelForm):

    class Meta:
        model = Connection
        fields = ('plan',)

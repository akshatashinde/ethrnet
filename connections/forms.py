from django import forms
from connections.models import Connection


class ConnectionForm(forms.ModelForm):

    class Meta:
        model = Connection
        fields = ["user_name", "company_name", "email", "plan",
                  "address", "landmark", "birth_date",
                  "gender","id_proof_types","id_proof",
                  "address_proof_types","address_proof","is_active"]
        widgets = {
            'id_proof_types': forms.Select(attrs={'id': 'id_proof_types'}),
            'address_proof_types': forms.Select(attrs={'id': 'address_proof_types'}),
        }

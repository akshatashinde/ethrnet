from django import forms
from plans.models import Plans


class ProductForm(forms.ModelForm):

    class Meta:
        model = Plans
        fields = ["plan_type", "price", "duration", "download_speed",
                  "FUP_limit", "post_FUP_speed", "installation_charges",
                  "subscription_amount"]
        widgets = {
            'plan_type': forms.Select(attrs={'id': 'plan_type'}),
        }

from django import forms
from fileupload.models import Picture


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        exclude = []

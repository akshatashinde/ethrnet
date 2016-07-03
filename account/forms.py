from django import forms
from account.models import Branch, UserProfile


class BranchForm(forms.ModelForm):

    class Meta:
        model = Branch


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

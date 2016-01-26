from django import forms
from .models import UserAddress, UserProfile
from django.contrib.auth.models import User
from functools import partial
from django.contrib.auth.forms import (AuthenticationForm,
                                       ReadOnlyPasswordHashField)

DateInput = partial(forms.DateInput, {'class': 'datep'})


class UserAddressForm(forms.ModelForm):
	class Meta:
		model = UserAddress
		fields = ["address", 
				"address2", 
				"city", 
				"state",
				"zipcode", 
				"phone"]


class UserProfileForm(forms.ModelForm):
	dob = forms.DateField(widget=DateInput())
	class Meta:
		model = UserProfile
		fields = ["first_name","last_name","mobile_no","gender","dob","profile_picture"]


class PPIUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='Password',
                                      widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password_repeat(self):
        password = self.cleaned_data.get("password")
        password_repeat = self.cleaned_data.get("password_repeat")

        if password and password_repeat and password != password_repeat:
            raise forms.ValidationError(_("Password dont match"))
        # else
        return password_repeat

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(_("Username already Exists"))

    def save(self, commit=True):
        user = super(PPIUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


class PPIUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_staff', 'is_active')

    def clean_password(self):
        return self.initial["password"]

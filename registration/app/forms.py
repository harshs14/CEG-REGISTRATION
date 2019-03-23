from django import forms
from .models import *


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ('name', 'phone_number', 'email', 'address',)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone_number', 'enquiry')

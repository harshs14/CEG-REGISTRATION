from django import forms
from .models import *


class Register(forms.ModelForm):

    class Meta:
        model = Register
        fields = ('name', 'phone_number', 'email', 'address', 'event')


class Contact(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone_number', 'enquiry')

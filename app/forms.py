from django import forms
from .models import *


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ('name', 'email', 'address',)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'enquiry')

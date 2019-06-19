from django import forms
from .models import *


class RegisterForm(forms.ModelForm):

    captcha = forms.IntegerField(required=True)

    class Meta:
        model = Register
        fields = ('first_name', 'middle_name', 'last_name', 'gender', 'email', 'address', 'city', 'state', 'pincode', 'category',
                  'organisation', 'designation', 'captcha')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'enquiry')

import re
from django import forms
from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, error_messages={'name':"Your name is required to submit this form"})
    email = forms.EmailField(required=True, error_messages={"email":"Your email is required to submit this form"})
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Your phone is required must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17, required=True) # validators should be a li
    company = forms.CharField(required=False, max_length=150)
    message = forms.CharField(required=True, max_length=400)



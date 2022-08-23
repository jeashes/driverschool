from django.forms import ModelForm, forms
from .models import DriverApplication, Partnership
import re
from django.core.exceptions import ValidationError


class CreateApplicationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].empty_label = 'City not chosen'
        self.fields['driverschoolunit'].empty_label = 'Drive school not chosen'
        self.fields['course'].empty_label = 'Course not chosen'

    class Meta:
        model = DriverApplication
        fields = ['firstLast_name', 'phone_number', 'email', 'city', 'driverschoolunit', 'course']

    def clean_firstLast_name(self):
        fl_name = self.cleaned_data['firstLast_name']
        if re.findall(r"(^[А-ЩЬЮЯҐЄІЇа-щьюяґєії][А-ЩЬЮЯҐЄІЇа-щьюяґєії\s]{0,20}[А-ЩЬЮЯҐЄІЇа-щьюяґєії]$)", fl_name):
            return fl_name
        else:
            raise ValidationError('First and last name input not correctly')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if re.findall(r'^(?:\+38)?(0\d{9})$', phone_number):
            return phone_number
        else:
            raise ValidationError('Phone number was introduced not correctly')

    def clean_email(self):
        email = self.cleaned_data['email']
        if re.findall(r'^(.+)@(.+)$', email):
            return email
        else:
            raise ValidationError('Email was introduced not correctly')


class PartnershipForm(ModelForm):
    class Meta:
        model = Partnership
        fields = ['firstLast_name', 'phone_number', 'email', 'description']

    def clean_firstLast_name(self):
        fl_name = self.cleaned_data.get('firstLast_name')
        if re.findall(r"(^[А-ЩЬЮЯҐЄІЇа-щьюяґєії][А-ЩЬЮЯҐЄІЇа-щьюяґєії\s]{0,20}[А-ЩЬЮЯҐЄІЇа-щьюяґєії]$)", fl_name):
            return fl_name
        else:
            raise ValidationError('First and last name input not correctly')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if re.findall(r'^(?:\+38)?(0\d{9})$', phone_number):
            return phone_number
        else:
            raise ValidationError('Phone number was introduced not correctly')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.findall(r'^(.+)@(.+)$', email):
            return email
        else:
            raise ValidationError('Email was introduced not correctly')

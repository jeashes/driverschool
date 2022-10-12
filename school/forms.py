from django.forms import ModelForm, TextInput
from .models import DriverApplication, Partnership
import re
from django.core.exceptions import ValidationError


class CreateApplicationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].empty_label = 'Оберіть місто'
        self.fields['driverschoolunit'].empty_label = 'Drive school not chosen'
        self.fields['course'].empty_label = 'Course not chosen'

    class Meta:
        model = DriverApplication
        fields = ['firstLast_name', 'phone_number', 'email', 'city', 'driverschoolunit', 'course']
        widgets = {
            'firstLast_name': TextInput(attrs={'placeholder': "Введіть Прізвище Ім'я"}),
            'phone_number': TextInput(attrs={'placeholder': '+38XXXXXXXXXX'}),
            'email': TextInput(attrs={'placeholder': 'email@example.com '}),
        }

    def clean_firstLast_name(self):
        fl_name = self.cleaned_data['firstLast_name']
        if re.findall(r"(^[А-ЩЬЮЯҐЄІЇа-щьюяґєії][А-ЩЬЮЯҐЄІЇа-щьюяґєії\s]{0,20}[А-ЩЬЮЯҐЄІЇа-щьюяґєії]$)", fl_name):
            return fl_name
        else:
            raise ValidationError("Прізвище та Ім'я введені не корректно")

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if re.findall(r'^(?:\+38)?(0\d{9})$', phone_number):
            return phone_number
        else:
            raise ValidationError('Номер телефону введено не корректно')

    def clean_email(self):
        email = self.cleaned_data['email']
        if re.findall(r'^(.+)@(.+)$', email):
            return email
        else:
            raise ValidationError('Gmail введено не корректно')


class PartnershipForm(ModelForm):
    class Meta:
        model = Partnership
        fields = ['firstLast_name', 'phone_number', 'email', 'description']
        widgets = {
            'firstLast_name': TextInput(attrs={'placeholder': "Введіть Прізвище Ім'я"}),
            'phone_number': TextInput(attrs={'placeholder': '+38XXXXXXXXXX'}),
            'email': TextInput(attrs={'placeholder': 'email@example.com'}),
        }

    def clean_firstLast_name(self):
        fl_name = self.cleaned_data.get('firstLast_name')
        if re.findall(r"(^[А-ЩЬЮЯҐЄІЇа-щьюяґєії][А-ЩЬЮЯҐЄІЇа-щьюяґєії\s]{0,20}[А-ЩЬЮЯҐЄІЇа-щьюяґєії]$)", fl_name):
            return fl_name
        else:
            raise ValidationError("Прізвище та Ім'я введені не корректно")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if re.findall(r'^(?:\+38)?(0\d{9})$', phone_number):
            return phone_number
        else:
            raise ValidationError('Номер телефону введено не корректно')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.findall(r'^(.+)@(.+)$', email):
            return email
        else:
            raise ValidationError('Gmail введено не корректно')

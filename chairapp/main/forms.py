from django.forms import ModelForm
from django import forms
from .models import UserInformation
from phonenumber_field.formfields import PhoneNumberField


class UserInformationForm(ModelForm):
    name = forms.CharField()
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),
                                    label="Phone number",
                                    required=True)
    mail = forms.EmailField()
    city = forms.CharField()
    street = forms.IntegerField()
    floor = forms.IntegerField()
    house = forms.IntegerField()
    apartment = forms.IntegerField()
    comment = forms.TextInput()

    class Meta:
        model = UserInformation
        fields = ['name', 'phone_number', 'mail', 'city', 'street', 'floor', 'house', 'apartment', 'comment']

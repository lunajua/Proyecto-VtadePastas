from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Address
from django import forms
from django.forms import inlineformset_factory
from django.forms import BaseFormSet, HiddenInput

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['calle', 'ciudad', 'estado', 'codigo_postal']

class CustomAddressFormSet(BaseFormSet):
    def get_deletion_widget(self):
        return HiddenInput()

AddressFormSet = inlineformset_factory(CustomUser, Address, form=AddressForm, formset=CustomAddressFormSet, can_delete=True, extra=1)
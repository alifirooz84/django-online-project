from django import forms
from .models import PhoneNumber

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number']
        widgets = {
            'number': forms.TextInput(attrs={'placeholder': 'شماره تلفن خود را وارد کنید'}),
        }

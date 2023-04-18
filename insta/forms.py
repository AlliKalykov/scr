from django import forms
from .models import Country, City

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'code', 'picture')

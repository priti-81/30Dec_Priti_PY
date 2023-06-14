from django import forms
from .models import productdetails


class productForm(forms.ModelForm):
    class Meta:
        model=productdetails
        fields='__all__'

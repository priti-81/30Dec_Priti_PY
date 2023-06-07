from django import forms
from .models import product,productdetails

class productForm(forms.ModelForm):
    class Meta:
        model=product,productdetails
        fields='__all__'

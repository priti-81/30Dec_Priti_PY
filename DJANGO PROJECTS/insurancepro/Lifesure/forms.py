from django import forms
from .models import Addpolicy,Login,policyTable

class policyForm(forms.ModelForm):
    class Meta:
        model=Addpolicy
        fields=['policynames']

class loginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'

class signupForm (forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'

class userpolicyForm(forms.ModelForm):
    class Meta:
        model=policyTable
        fields='__all__'
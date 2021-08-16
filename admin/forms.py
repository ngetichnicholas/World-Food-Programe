from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields
from wfp_app.models import *


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=("username","email","password1","password2")
        help_texts = {
            "username":None,
        }


class CountryForm(forms.ModelForm):
    class Meta:
      model = Country
      fields = ['iso_code','name']

class OfficeForm(forms.ModelForm):
    class Meta:
      model = Intervention
      fields = ['name','code_name','start_date','end_date']

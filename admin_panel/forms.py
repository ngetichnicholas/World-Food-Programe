from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields
from wfp_app.models import *

class CountryForm(forms.ModelForm):
    class Meta:
      model = Country
      fields = ['iso_code','name']

class OfficeForm(forms.ModelForm):
    class Meta:
      model = Intervention
      fields = ['name','code_name','office_id','start_date','end_date']

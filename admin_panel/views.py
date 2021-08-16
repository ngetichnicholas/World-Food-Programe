from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.
@login_required
def admin(request):
    return render(request,'admin/admin.html')

# Add country
@login_required
def add_country(request):
  if request.method == 'POST':
    country_form=CountryForm(request.POST)
    if country_form.is_valid():
      country = country_form.save(commit=False)
      country.save()
      messages.success(request,'New country added')
      return redirect('admin')

  else:
    country_form = CountryForm()
  context = {
    'country_form': country_form,
    }
  return render(request,"admin/country.html",context)

# Add office
@login_required
def add_office(request):
  if request.method == 'POST':
    office_form=OfficeForm(request.POST)
    if office_form.is_valid():
      office = office_form.save(commit=False)
      office.save()
      messages.success(request,'New office added')
      return redirect('admin')

  else:
    office_form = OfficeForm()
  context = {
    'office_form': office_form,
    }
  return render(request,"admin/office.html",context)
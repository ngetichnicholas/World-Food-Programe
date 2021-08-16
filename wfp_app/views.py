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
def signup(request):
    if request.method=='POST':
        user_form=UserSignUpForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.refresh_from_db()
            user.email = user_form.cleaned_data.get('email')
            group, created = Group.objects.get_or_create(name='admin')
            group = Group.objects.get(name = 'admin')
            user.groups.add(group)
            user.save()
            return redirect('login')
    else:
        user_form=UserSignUpForm()
        
    return render(request,'registration/signup.html',{'user_form':user_form})


#Login users
def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
        auth_login(request, user)
        messages.info(request, f"You are now logged in as {username}")
        return redirect('admin')
      else:
        messages.error(request, "Invalid username or password.")
    else:
      messages.error(request, "Invalid username or password.")
  form = AuthenticationForm()
  return render(request = request,template_name = "registration/login.html",context={"form":form})
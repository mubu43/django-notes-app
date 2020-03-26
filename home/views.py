# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#added for http response

from django.http import HttpResponse

#get model class from models file
from notes.models import Note

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def home(request):
    notes = Note.objects.all().order_by('date')
    return render(request, 'home.html', {'notes': notes})

def signupview(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect('notes:list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', { 'form': form })

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('form is valid')
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                print('hitting if block with login')
                return redirect(request.POST.get('next'))
            else:
               print('hitting else block with login')
               return redirect('notes:list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })

def logoutview(request):
    if request.method == 'POST':
            logout(request)
            return redirect('home:login')
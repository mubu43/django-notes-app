# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from . import forms


@login_required(login_url="login/")
def notes_list(request):
    notes = Note.objects.filter(username=request.user);
    return render(request, 'notes_list.html', { 'notes': notes })


@login_required(login_url="login/")
def notes_add(request):
    if request.method == 'POST':
        form = forms.AddNote(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()
            return redirect('notes:list')
    else:
        form = forms.AddNote()
    return render(request, 'notes_add.html', { 'form': form })

@login_required(login_url="login/")
def notes_edit(request, id):
    if request.method == 'POST':
        form = forms.AddNote(request.POST)
        if form.is_valid():
            instance=Note.objects.get(id=id)
            instance.title=request.POST.get('title')
            instance.content=request.POST.get('content')
            instance.save()
            return redirect('notes:list')
    else:
        instance = Note.objects.get(id=id)
        data = {'title': instance.title, 'content': instance.content}
        print('constructed dictionary')
        form = forms.AddNote(data)
        print('form created beginning render')
    return render(request, 'notes_edit.html', { 'form': form, 'id':id })
    

@login_required(login_url="login/")
def notes_delete(request, id):
    instance = Note.objects.get(id=id)
    instance.delete()
    notes = Note.objects.filter(username=request.user)
    return redirect('notes:list')


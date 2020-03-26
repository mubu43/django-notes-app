from django import forms
from . import models

class AddNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'content',]
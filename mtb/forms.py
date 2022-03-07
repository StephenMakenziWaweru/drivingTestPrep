from django import forms
from .models import Notes

class NotesUpdateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'link']

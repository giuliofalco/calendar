from django import forms
from .models import *

class DayEntryForm(forms.ModelForm):
    class Meta:
        model = DayEntry
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }

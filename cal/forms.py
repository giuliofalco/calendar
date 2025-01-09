from django import forms
from .models import *

class DayEntryForm(forms.ModelForm):
    class Meta:
        model = DayEntry
        fields = ['content_left', 'content_right']
        widgets = {
            'content_left': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
            'content_right': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }

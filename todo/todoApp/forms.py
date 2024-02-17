from django import forms
from todoApp.models import TODO

from django import forms
from .models import TODO

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'description', 'status', 'priority', 'date', 'time']  # Include 'time' field in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Use DateInput widget to allow date selection
            'time': forms.TimeInput(attrs={'type': 'time'}),  # Use TimeInput widget to allow time selection
        }

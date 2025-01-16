from django import forms
from .models import Colleague

class ColleagueForm(forms.ModelForm):
    class Meta:
        model = Colleague
        fields = ['name', 'position', 'photo']

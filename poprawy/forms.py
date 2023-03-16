from django import forms
from django.forms import ModelForm
from .models import Uczen, Poprawa

class Zgloszenie(ModelForm):
    class Meta:
        model = Poprawa
        fields = ('przedmiot', 'temat', 'nauczyciel', 'data')
        widgets = {
            'temat': forms.TextInput(attrs={'placeholder': 'Temat'}),
            'data': forms.TextInput(attrs={'placeholder': 'Data i czas'}),
        }
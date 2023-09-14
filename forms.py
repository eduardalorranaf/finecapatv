from django import forms
from django.forms import ModelForm
from .models import Reserva


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px'}),
            'categoria_empresa' : forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px'}),
            'cnpj' : forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px'}),
            
        }

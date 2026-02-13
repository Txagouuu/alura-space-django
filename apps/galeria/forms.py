
from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class meta:
        model = Fotografia
        exclude = ['publicada']

        wigets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateTimeInput(
                format = '%d/%m/%Y',
                attrs={
                    type: 'date',
                    'class': 'form-control'
                    }),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
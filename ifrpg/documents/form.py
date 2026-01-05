from django import forms
from .models import Documentos

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['titulo', 'link', 'player']
        labels = {'titulo': 'Título do Documento', 'link': 'Link do Documento', 'player': 'Jogador'}
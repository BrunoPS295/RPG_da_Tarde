from django import forms 
from .models import Documentos
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['titulo', 'arquivo', 'permitidos']
        labels = {'titulo': 'Título', 'arquivo': 'Arquivo', 'permitidos': 'Usuários Permitidos'}
        widgets = {
            'permitidos': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['permitidos'].queryset = User.objects.exclude(id=user.id)

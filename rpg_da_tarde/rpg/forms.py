
from django import forms
from .models import Ficha

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = [ 
            'rpg',
            'nome', 
            'classe', 
            'antecedente', 
            'raca', 
            'alinhamento', 
            'experiencia',

            'inspiracao',    
            'max_pv',
            'i_pv',
            'dado_de_vida',
            'bonus_de_proficiencia',

            'forca', 
            'destreza',
            'constituicao',
            'inteligencia',
            'sabedoria',
            'carisma'
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
  
    
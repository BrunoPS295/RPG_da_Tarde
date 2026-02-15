
from django import forms
from .models import Ficha
from .models import Ataques

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
            'temp_pv',
            'i_pv',
            'dado_de_vida',
            'bonus_de_proficiencia',

            'forca', 
            'destreza',
            'constituicao',
            'inteligencia',
            'sabedoria',
            'carisma',
            'morte',
            'textao',
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class AtaqueForm(forms.ModelForm):
    class Meta:
        model = Ataques
        fields = [
            'ficha',
            'nome_ataque',
            'acerto_ataque',
            'dano_ataque',
        ]

class gm_fichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = [  
        'id',
        'experiencia',
        'inspiracao', 
        'atual_pv',
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


  
    
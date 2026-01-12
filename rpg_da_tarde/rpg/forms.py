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

            #'pontos_de_vida_maximos',
            #'dado_de_vida',

            #'força', 
            #'destreza',
            #'constituição',
            #'inteligencia',
            #'sabedoria',
            #'carisma'
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
  
    
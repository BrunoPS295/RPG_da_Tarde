
from django import forms
from django.core.exceptions import ValidationError
from .models import Ficha
from .models import Ataques
from .models import Itens
from .models import RPGmodel

class FichaForm(forms.ModelForm):
    rpg = forms.CharField(label='Chave do RPG', required=True, max_length=10)

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
            'atual_pv',
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
        instance = kwargs.get('instance')
        if instance and hasattr(instance, 'rpg') and instance.rpg:
            self.fields['rpg'].initial = instance.rpg.key

    def clean_rpg(self):
        key = self.cleaned_data.get('rpg')
        if not key:
            raise ValidationError('Informe a chave do RPG.')
        try:
            return RPGmodel.objects.get(key=key)
        except RPGmodel.DoesNotExist:
            raise ValidationError('Chave de RPG inválida.')

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

class ItemForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = [
            'ficha',
            'nome',
            'atributo_modificado',
            'atributo_modificado_text',
            'modificador',
            'documento',
            'quantidade',
            'equipado',
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['ficha'].queryset = Ficha.objects.filter(rpg__mestre=user)

class rpgForm(forms.ModelForm):
    class Meta:
        model = RPGmodel
        fields = [
            'rpg_nome',
            'jogadores',
        ]
        widgets = {
            'jogadores': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(rpgForm, self).__init__(*args, **kwargs)





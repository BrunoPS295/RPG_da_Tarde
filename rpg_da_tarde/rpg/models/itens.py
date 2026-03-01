from django.db import models
from django.contrib.auth.models import User
modificadores_atributos = [
    ('atrforca', 'Força'),
    ('atrdestreza', 'Destreza'),
    ('atrconstituicao', 'Constituição'),
    ('atrinteligencia', 'Inteligência'),
    ('atrsabedoria', 'Sabedoria'),
    ('atrcarisma', 'Carisma'),

    ('salvaforca', 'Salva_Força'),
    ('salvadestreza', 'Salva_Destreza'),
    ('salvaconstituicao', 'Salva_Constituição'),
    ('salvainteligencia', 'Salva_Inteligência'),
    ('salvasabedoria', 'Salva_Sabedoria'),
    ('salvacarisma', 'Salva_Carisma'),

    ('periacrobacia', 'Acrobacia'),
    ('periarcanismo', 'Arcanismo'),
    ('periatletismo', 'Atletismo'),
    ('periatuacao', 'Atuação'),
    ('perienganacao', 'Enganação'),
    ('perifurtividade', 'Furtividade'),
    ('perihistoria', 'História'),
    ('periintimidacao', 'Intimidação'),
    ('periintuicao', 'Intuição'),
    ('periinvestigacao', 'Investigação'),
    ('perianimais', 'Adestrar Animais'),
    ('perimedicina', 'Medicina'),
    ('perinatureza', 'Natureza'),
    ('peripercepcao', 'Percepção'),
    ('peripersuasao', 'Persuasão'),
    ('periprestidigitacao', 'Prestidigitação'),
    ('perireligiao', 'Religião'),
    ('perisobrevivencia', 'Sobrevivência'),

    ('ca', 'CA'),
    ('iniciativa', 'Iniciativa'),
    ('deslocamento', 'Deslocamento'),
    ('max_pv', 'Vida Máxima'),


]

class Itens(models.Model):
    rpg_item = models.ForeignKey('RPGmodel', on_delete=models.CASCADE)
    ficha = models.ForeignKey('Ficha', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=True, null=True)
    atributo_modificado = models.CharField(choices=modificadores_atributos,blank=True, null=True)
    atributo_modificado_text = models.CharField(max_length=100, blank=True, null=True)
    modificador = models.CharField(max_length=100, blank=True, null=True)
    documento = models.FileField(upload_to='documentos/itens', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Itens"

    def __str__(self):
        if self.nome:
            return self.nome
        return f"Item {self.id}"
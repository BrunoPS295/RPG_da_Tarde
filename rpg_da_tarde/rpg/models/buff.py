from django.db import models

modificadores_atributos = [
    ('Força', 'Força'),
    ('Destreza', 'Destreza'),
    ('Constituição', 'Constituição'),
    ('Inteligência', 'Inteligência'),
    ('Sabedoria', 'Sabedoria'),
    ('Carisma', 'Carisma'),

    ('CA', 'CA'),
    ('Iniciativa', 'Iniciativa'),
    ('deslocamento', 'deslocamento'),
    ('max_pv', 'vida máxima'),

    ('dano_perfurante', 'dano a perfurante'),
    ('dano_cortante', 'dano a cortante'),
    ('dano_contundente', 'dano a contundente'),
    ('dano_fogo', 'dano a fogo'),
    ('dano_frio', 'dano a frio'),
    ('dano_eletricidade', 'dano a eletricidade'),
    ('dano_veneno', 'dano a veneno'),
    ('dano_necrotico', 'dano a necrotico'),
    ('dano_radiante', 'dano a radiante'),
    ('dano_psiquico', 'dano a psiquico'),

    ('res_perfurante', 'resistencia a perfurante'),
    ('res_cortante', 'resistencia a cortante'),
    ('res_contundente', 'resistencia a contundente'),
    ('res_fogo', 'resistencia a fogo'),
    ('res_frio', 'resistencia a frio'),
    ('res_eletricidade', 'resistencia a eletricidade'),
    ('res_veneno', 'resistencia a veneno'),
    ('res_necrotico', 'resistencia a necrotico'),
    ('res_radiante', 'resistencia a radiante'),
    ('res_psiquico', 'resistencia a psiquico'),

    ('Esp1', 'Especial 1'),
    ('Esp2', 'Especial 2'),
    ('Esp3', 'Especial 3'),
]

class Buff(models.Model):
    nome = models.CharField(max_length=100)
    modificado_atributo = models.CharField(choices=modificadores_atributos)
    multiplicador = models.FloatField(blank=True, null=True)
    modificador = models.IntegerField(blank=True, null=True)
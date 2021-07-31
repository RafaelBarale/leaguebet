from django.db import models


class Clube(models.Model):
    UF_CHOICES = [
        ["AC", "Acre"],
        ["AL", "Alagoas"],
        ["AP", "Amapá"],
        ["AM", "Amazonas"],
        ["BA", "Bahia"],
        ["CE", "Ceará"],
        ["DF", "Distrito Federal"],
        ["ES", "Espírito Santo"],
        ["GO", "Goiás"],
        ["MA", "Maranhão"],
        ["MT", "Mato Grosso"],
        ["MS", "Mato Grosso do Sul"],
        ["MG", "Minas Gerais"],
        ["PA", "Pará"],
        ["PB", "Paraíba"],
        ["PR", "Paraná"],
        ["PE", "Pernambuco"],
        ["PI", "Piauí"],
        ["RJ", "Rio de Janeiro"],
        ["RN", "Rio Grande do Norte"],
        ["RS", "Rio Grande do Sul"],
        ["RO", "Rondônia"],
        ["RR", "Roraima"],
        ["SC", "Santa Catarina"],
        ["SP", "São Paulo"],
        ["SE", "Sergipe"],
        ["TO", "Tocantins"]
    ]
    nome = models.CharField(max_length=20, null=False, blank=False)
    nome_abreviado = models.CharField(max_length=3, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=UF_CHOICES)
    escudo = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.nome

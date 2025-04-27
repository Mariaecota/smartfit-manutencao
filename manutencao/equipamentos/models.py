from django.db import models

class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('verde', 'Verde - Funcionando'),
        ('amarelo', 'Amarelo - Com defeito parcial'),
        ('vermelho', 'Vermelho - Fora de uso'),
    ]

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='verde')
    defeito_relatado = models.TextField(blank=True, null=True)
    data_chamado = models.DateField(auto_now_add=True)
    previsao_conserto = models.DateField(blank=True, null=True)
    tecnico_responsavel = models.CharField(max_length=100, blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

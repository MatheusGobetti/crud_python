from django.db import models

# Create your models here.
class Residencias(models.Model):
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=80)
    cidade = models.CharField(max_length=25)    
    estado = models.CharField(max_length=2)
    preco_aluguel = models.FloatField(max_length=15)
    preco_venda = models.FloatField(max_length=15)
    cpf_proprietario = models.CharField(max_length=11)

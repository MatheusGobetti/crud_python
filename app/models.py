from django.db import models

# Create your models here.
class Residencias(models.Model):
    endereco = models.CharField(max_length=200, null=True)
    numero = models.IntegerField(null=True)
    complemento = models.CharField(max_length=30, null=True)
    bairro = models.CharField(max_length=80, null=True)
    cidade = models.CharField(max_length=25, null=True)    
    estado = models.CharField(max_length=2, null=True)
    preco_aluguel = models.FloatField(max_length=15, null=True)
    preco_venda = models.FloatField(max_length=15, null=True)
    cpf_proprietario = models.CharField(max_length=11, null=True)

class Usuarios(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)

class Proprietarios(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.IntegerField()
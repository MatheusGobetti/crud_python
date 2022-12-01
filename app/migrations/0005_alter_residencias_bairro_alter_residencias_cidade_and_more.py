# Generated by Django 4.1.2 on 2022-12-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_proprietarios_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencias',
            name='bairro',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='cidade',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='complemento',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='cpf_proprietario',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='endereco',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='estado',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='numero',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='preco_aluguel',
            field=models.FloatField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='residencias',
            name='preco_venda',
            field=models.FloatField(max_length=15, null=True),
        ),
    ]

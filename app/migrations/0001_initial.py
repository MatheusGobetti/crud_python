# Generated by Django 4.1.2 on 2022-11-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=200)),
                ('numero', models.IntegerField(max_length=7)),
                ('complemento', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=80)),
                ('cidade', models.CharField(max_length=7)),
                ('estado', models.CharField(max_length=2)),
                ('preco_aluguel', models.FloatField(max_length=15)),
                ('preco_venda', models.FloatField(max_length=15)),
                ('cpf_proprietario', models.CharField(max_length=11)),
            ],
        ),
    ]

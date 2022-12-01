# Generated by Django 4.1.2 on 2022-11-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_residencias_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('telefone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
    ]
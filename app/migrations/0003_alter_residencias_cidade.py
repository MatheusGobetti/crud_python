# Generated by Django 4.1.2 on 2022-11-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_residencias_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencias',
            name='cidade',
            field=models.CharField(max_length=25),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-21 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Continente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='continente',
            options={'ordering': ['Nombre'], 'verbose_name': 'Continente', 'verbose_name_plural': 'Continentes'},
        ),
    ]

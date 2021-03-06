# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-18 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0024_auto_20170618_0120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atencion',
            options={'permissions': (('atencion', 'Can ALL atencion'),), 'verbose_name': 'Atencion', 'verbose_name_plural': 'Atenciones'},
        ),
        migrations.AlterModelOptions(
            name='atenciones',
            options={'permissions': (('atenciones', 'Can ALL atenciones'),), 'verbose_name': 'Atencione', 'verbose_name_plural': 'Atencioness'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('clientes', 'Can ALL clientes'),), 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='colamedica',
            options={'permissions': (('colamedica', 'Can ALL colamedica'),), 'verbose_name': 'Cola Medica', 'verbose_name_plural': 'Colas Medicas'},
        ),
        migrations.AlterModelOptions(
            name='historial',
            options={'permissions': (('historia', 'Can ALL historia'),), 'verbose_name': 'Historia', 'verbose_name_plural': 'Historias'},
        ),
        migrations.AlterModelOptions(
            name='mascota',
            options={'permissions': (('mascota', 'Can ALL mascota'), ('mascota_perfil', 'Can LIST perfil')), 'verbose_name': 'Mascota', 'verbose_name_plural': 'Mascotas'},
        ),
        migrations.AlterModelOptions(
            name='vacunacion',
            options={'permissions': (('vacunaciones', 'Can ALL vacunaciones'),), 'verbose_name': 'vacunacion', 'verbose_name_plural': 'vacunaciones'},
        ),
    ]

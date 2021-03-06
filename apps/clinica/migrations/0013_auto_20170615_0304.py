# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-15 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0012_auto_20170615_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivosAdjuntos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='Archivos', verbose_name='Archivo')),
                ('created_time', models.TimeField(auto_now_add=True, verbose_name='Hora Creada')),
                ('created_ath', models.DateField(auto_now_add=True, verbose_name='Fecha Creada')),
            ],
            options={
                'verbose_name_plural': 'Archivos',
                'verbose_name': 'Archivo',
            },
        ),
        migrations.RemoveField(
            model_name='atenciones',
            name='archivo',
        ),
        migrations.AddField(
            model_name='archivosadjuntos',
            name='atenciones',
            field=models.ManyToManyField(to='clinica.Atenciones'),
        ),
    ]

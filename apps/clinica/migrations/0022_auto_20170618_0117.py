# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-18 06:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0021_auto_20170618_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('clientes', 'Can ALL clientes'), ('clientes', 'Can CREATE clientes'), ('clientes', 'Can DELETE clientes'), ('clientes', 'Can UPDATE clientes'), ('clientes', 'Can LIST clientes')), 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]

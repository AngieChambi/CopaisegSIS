# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-18 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20170618_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'permissions': (('venta', 'Can ALL venta'),), 'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
    ]

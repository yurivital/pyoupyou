# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_auto_20170410_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='planned_date',
            field=models.DateField(blank=True, null=True, verbose_name='Planned date'),
        ),
    ]
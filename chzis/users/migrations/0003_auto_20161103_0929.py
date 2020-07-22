# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-03 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_load_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peopleprofile',
            name='default_congregation',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='congregation.Congregation'),
        ),
    ]
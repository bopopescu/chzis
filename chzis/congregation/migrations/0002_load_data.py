# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 08:08
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command


def load_fixtures(state_apps, schema_editor):
    call_command('loaddata', 'congregations', 'congregations_members_pie_ka')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('congregation', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixtures)
    ]
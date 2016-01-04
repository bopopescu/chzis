# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 23:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_add_superuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Congregation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255, null=True)),
                ('number', models.IntegerField(null=True)),
                ('circuit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CongregationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('baptism_date', models.DateField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('servant', models.BooleanField(default=False)),
                ('elder', models.BooleanField(default=False)),
                ('coordinator', models.BooleanField(default=False)),
                ('pioneer', models.BooleanField(default=False)),
                ('school_allow', models.BooleanField(default=False)),
                ('master', models.BooleanField(default=False)),
                ('slave', models.BooleanField(default=False)),
                ('reader_only', models.BooleanField(default=False)),
                ('lector', models.BooleanField(default=False)),
                ('sound_sysop', models.BooleanField(default=False)),
                ('last_modification', models.DateTimeField(auto_now_add=True, null=True)),
                ('congregation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='congregation.Congregation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='congregation',
            name='coordinator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='congregation.CongregationMember'),
        ),
    ]

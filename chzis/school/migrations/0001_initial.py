# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('meetings', '0002_load_data'),
    ]

    operations = [
        migrations.CreateModel(
                name='Background',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('number', models.IntegerField()),
                    ('name', models.CharField(max_length=255)),
                    ('description', models.CharField(max_length=255, null=True)),
                    ('last_modification', models.DateTimeField(auto_now=True, null=True)),
                ],
                options={
                    'ordering': ['number'],
                },
        ),
        migrations.CreateModel(
                name='Lesson',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('number', models.IntegerField()),
                    ('name', models.CharField(max_length=255)),
                    ('reading', models.BooleanField(default=False)),
                    ('demo', models.BooleanField(default=False)),
                    ('discourse', models.BooleanField(default=False)),
                    ('book_page', models.CharField(max_length=255, null=True)),
                    ('description', models.TextField(null=True)),
                    ('last_modification', models.DateTimeField(auto_now=True, null=True)),
                ],
                options={
                    'ordering': ['number'],
                },
        ),
        migrations.CreateModel(
                name='SchoolTask',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('subordinate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                        related_name='subordinate_person', to='congregation.CongregationMember')),
                    ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                        related_name='supervisor_person', to='congregation.CongregationMember')),
                    ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_person', to='congregation.CongregationMember')),
                    ('lesson_passed', models.NullBooleanField()),
                    ('lesson_passed_date', models.DateTimeField(blank=True, null=True)),
                    ('description', models.TextField(blank=True, null=True)),
                    ('last_modification', models.DateTimeField(auto_now=True, null=True)),
                    ('background', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                     to='school.Background')),
                    ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Lesson')),
                    ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               to='meetings.MeetingTask')),
                ],
                options={
                    'permissions': (('can_view_all_tasks', 'Can see all available tasks'),
                                    ('can_judge_tasks', 'Can judge presented tasks by popele')),
                },
        ),
    ]

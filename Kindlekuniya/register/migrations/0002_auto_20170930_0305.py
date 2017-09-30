# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('email', models.EmailField(default=None, max_length=120, unique=True)),
                ('firstName', models.CharField(default=None, max_length=120)),
                ('lastName', models.CharField(default=None, max_length=120)),
                ('password', models.CharField(default=None, max_length=128)),
                ('phoneNO', models.IntegerField(default=None)),
            ],
        ),
        migrations.DeleteModel(
            name='userProfile',
        ),
    ]

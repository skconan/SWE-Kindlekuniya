# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('userID', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('email', models.EmailField(default='Example kindlekuniya@gmail.com', max_length=120, unique=True)),
                ('firstName', models.CharField(default=None, max_length=120)),
                ('lastName', models.CharField(default=None, max_length=120)),
                ('password', models.CharField(default=None, max_length=128)),
                ('phoneNO', models.IntegerField(default=None)),
            ],
        ),
    ]

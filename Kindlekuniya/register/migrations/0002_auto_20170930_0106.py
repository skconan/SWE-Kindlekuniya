# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=None, max_length=120, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20170930_0106'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userProfile',
            new_name='User',
        ),
    ]
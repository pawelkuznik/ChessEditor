# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chesseditor', '0005_auto_20170524_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='move_number',
            field=models.IntegerField(default=models.AutoField(primary_key=True, serialize=False)),
        ),
    ]
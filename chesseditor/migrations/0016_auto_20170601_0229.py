# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chesseditor', '0015_auto_20170530_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moves',
            name='states_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chesseditor.States'),
        ),
    ]
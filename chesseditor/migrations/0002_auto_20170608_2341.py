# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chesseditor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='orgaznier',
            new_name='organizer_of_tournament',
        ),
        migrations.AlterField(
            model_name='chessparty',
            name='chessparty_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID partii'),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleapi', '0005_auto_20151010_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='genero',
        ),
        migrations.AlterField(
            model_name='accidente',
            name='latitud',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='accidente',
            name='longitud',
            field=models.FloatField(),
        ),
    ]

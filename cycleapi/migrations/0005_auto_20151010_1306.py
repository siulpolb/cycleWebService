# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleapi', '0004_auto_20151010_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidente',
            name='latitud',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='accidente',
            name='longitud',
            field=models.CharField(max_length=20),
        ),
    ]

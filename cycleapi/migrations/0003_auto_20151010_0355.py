# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleapi', '0002_auto_20151010_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.TextField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.TextField(unique=True, max_length=15),
        ),
    ]

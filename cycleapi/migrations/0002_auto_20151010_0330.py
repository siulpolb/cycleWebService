# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accidente',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Accidente',
        ),
    ]

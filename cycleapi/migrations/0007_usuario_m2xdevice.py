# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleapi', '0006_auto_20151120_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='m2xDevice',
            field=models.TextField(default='hola', max_length=100),
            preserve_default=False,
        ),
    ]

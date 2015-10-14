# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleapi', '0003_auto_20151010_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accidente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(default='H', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accidente',
            name='usuario',
            field=models.ForeignKey(related_name='accidentes', to='cycleapi.Usuario'),
        ),
    ]

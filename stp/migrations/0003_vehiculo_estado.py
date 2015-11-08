# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stp', '0002_auto_20150824_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='estado',
            field=models.CharField(default='disponible', max_length=16),
            preserve_default=False,
        ),
    ]

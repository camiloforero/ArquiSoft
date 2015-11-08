# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencia',
            name='tranvia',
            field=models.ForeignKey(related_name='emergencias', default=1, to='stp.Tranvia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventogps',
            name='gps',
            field=models.ForeignKey(default=1, to='stp.GPS'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gps',
            name='mobibus',
            field=models.ForeignKey(related_name='dispositivos', to='stp.Mobibus', null=True),
        ),
    ]

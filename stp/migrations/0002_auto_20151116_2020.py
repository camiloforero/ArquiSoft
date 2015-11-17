# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cedula', models.CharField(max_length=32)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user', models.OneToOneField(related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='vcub',
            name='usuario',
            field=models.ForeignKey(related_name='vcubs', to='stp.Usuario', null=True),
        ),
    ]

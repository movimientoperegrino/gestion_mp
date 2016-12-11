# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantelesxpersonas',
            name='titular',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='plantelesxpersonas',
            name='plantel_x_persona_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]

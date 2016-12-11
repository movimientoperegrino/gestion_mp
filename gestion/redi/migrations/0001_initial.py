# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('actividad_id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_fin', models.DateTimeField(null=True, blank=True)),
                ('fecha_inicio', models.DateTimeField(null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('puntuacion', models.IntegerField()),
            ],
            options={
                'db_table': 'actividades',
                'managed': True,
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='ActividadesTipos',
            fields=[
                ('tipo_id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'actividades_tipos',
                'managed': True,
                'verbose_name_plural': 'Tipos de actividades',
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('persona_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('apellido', models.CharField(max_length=255, null=True, blank=True)),
                ('numero_contacto', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('cedula', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('fecha_retiro_encuentro', models.DateField(null=True, blank=True)),
                ('fecha_retiro_crecimiento', models.DateField(null=True, blank=True)),
                ('fecha_escuela_dirigentes', models.DateField(null=True, blank=True)),
                ('estado_civil', models.CharField(max_length=255, null=True, blank=True)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('activa', models.NullBooleanField()),
                ('edad', models.IntegerField(null=True, blank=True)),
                ('sexo', models.CharField(default='F', max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])),
            ],
            options={
                'db_table': 'personas',
                'managed': True,
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Planteles',
            fields=[
                ('plantel_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_fin', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'planteles',
                'managed': True,
                'verbose_name_plural': 'Planteles',
            },
        ),
        migrations.CreateModel(
            name='PlantelesXPersonas',
            fields=[
                ('plantel_x_persona_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('persona', models.ForeignKey(to='redi.Personas', null=True)),
                ('plantel', models.ForeignKey(to='redi.Planteles', null=True)),
            ],
            options={
                'db_table': 'planteles_x_personas',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='actividades',
            name='actividad_tipo',
            field=models.ForeignKey(blank=True, to='redi.ActividadesTipos', null=True),
        ),
        migrations.AddField(
            model_name='actividades',
            name='persona',
            field=models.ForeignKey(blank=True, to='redi.Personas', null=True),
        ),
    ]

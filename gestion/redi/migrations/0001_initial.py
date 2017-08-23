# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            name='ActividadPersona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default='E', max_length=1, choices=[('A', 'Acepto'), ('R', 'Rechazo'), ('E', 'Espera')])),
                ('titular', models.BooleanField(default=True)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('actividad', models.ForeignKey(to='redi.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadTipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'actividades_tipos',
                'managed': True,
                'verbose_name_plural': 'Tipos de actividades',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('user', models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'personas',
                'managed': True,
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='RetiroTipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'retiros_tipos',
                'managed': True,
                'verbose_name_plural': 'Tipos de retiros',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='actividadpersona',
            name='persona',
            field=models.ForeignKey(to='redi.Persona'),
        ),
        migrations.AddField(
            model_name='actividadpersona',
            name='rol',
            field=models.ForeignKey(to='redi.Rol'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='actividad_tipo',
            field=models.ForeignKey(blank=True, to='redi.ActividadTipo', null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='retiro_tipo',
            field=models.ForeignKey(blank=True, to='redi.RetiroTipo', null=True),
        ),
    ]

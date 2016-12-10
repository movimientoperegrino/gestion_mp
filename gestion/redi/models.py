# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from datetime import date
from django.contrib import admin
from django.db import models
from dateutil.relativedelta import relativedelta



class Actividades(models.Model):
    actividad_id = models.AutoField(primary_key=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    actividad_tipo = models.ForeignKey('ActividadesTipos', blank=True, null=True)
    puntuacion = models.IntegerField()
    persona = models.ForeignKey('Personas', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'actividades'
        verbose_name_plural = "Actividades"

    def __unicode__(self):
        return self.descripcion

class ActividadesTipos(models.Model):
    tipo_id = models.CharField(primary_key=True, max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'actividades_tipos'
        verbose_name_plural = "Tipos de actividades"

    def __unicode__(self):
        return self.descripcion


class Personas(models.Model):
    persona_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    numero_contacto = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    cedula = models.CharField(unique=True, max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_retiro_encuentro = models.DateField(blank=True, null=True)
    fecha_retiro_crecimiento = models.DateField(blank=True, null=True)
    fecha_escuela_dirigentes = models.DateField(blank=True, null=True)
    estado_civil = models.CharField(max_length=255, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    activa = models.NullBooleanField()
    edad = models.IntegerField(blank=True, null=True)

    @property
    def get_edad(self):
        return relativedelta(date.today(), self.fecha_nacimiento).years

    class Meta:
        managed = True
        db_table = 'personas'
        verbose_name_plural = "Personas"


    def __unicode__(self):
        return self.apellido + ", " + self.nombre

    def save(self, *args, **kwargs):
        self.edad = relativedelta(date.today(), self.fecha_nacimiento).years
        return super(Personas, self).save(*args, **kwargs)


class Planteles(models.Model):
    plantel_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planteles'
        verbose_name_plural = "Planteles"

    def __unicode__(self):
        return self.nombre


class PlantelesXPersonas(models.Model):
    plantel_x_persona_id = models.BigIntegerField(primary_key=True)
    plantel = models.ForeignKey(Planteles)
    persona = models.ForeignKey(Personas)

    class Meta:
        managed = False
        db_table = 'planteles_x_personas'

    @property
    def nombre_persona(self):
        return self.persona.apellido + ", " + self.persona.nombre



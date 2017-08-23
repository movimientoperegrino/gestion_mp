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
from django.contrib.auth.models import User




class Actividad(models.Model):
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    actividad_tipo = models.ForeignKey('ActividadTipo', blank=True, null=True)
    puntuacion = models.IntegerField()
    #persona = models.ForeignKey('Personas', blank=True, null=True)
    retiro_tipo = models.ForeignKey('RetiroTipo', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'actividades'
        verbose_name_plural = "Actividades"

    def __unicode__(self):
        return self.descripcion


class RetiroTipo(models.Model):
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'retiros_tipos'
        verbose_name_plural = "Tipos de retiros"

    def __unicode__(self):
        return self.descripcion


class ActividadTipo(models.Model):
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'actividades_tipos'
        verbose_name_plural = "Tipos de actividades"

    def __unicode__(self):
        return self.descripcion


class Persona(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    numero_contacto = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    cedula = models.CharField(unique=True, max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_retiro_encuentro = models.DateField(blank=True, null=True)
    fecha_retiro_crecimiento = models.DateField(blank=True, null=True)
    fecha_escuela_dirigentes = models.DateField(blank=True, null=True)
    SOLTERO = "SOLTERO"
    CASADO = "CASADO"
    DIVORCIADO = "DIVORCIADO"
    ESTADO_CIVIL_PERSONA = (
        (SOLTERO, 'SOLTERO/A'),
        (CASADO, 'CASADO/A'),
        (DIVORCIADO, 'DIVORCIADO/A')
    )
    estado_civil = models.CharField(max_length=255, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    activa = models.NullBooleanField()
    edad = models.IntegerField(blank=True, null=True)
    MASCULINO = "M"
    FEMENINO = "F"
    SEXO_PERSONA = (
        (MASCULINO, 'Masculino'),
        (FEMENINO,'Femenino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_PERSONA, default="F")
    user = models.OneToOneField(User, default=1)

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
        return super(Persona, self).save(*args, **kwargs)


class Rol(models.Model):
    descripcion = models.CharField(max_length=255)

    def __unicode__(self):
        return self.descripcion



class ActividadPersona(models.Model):
    actividad = models.ForeignKey(Actividad)
    persona = models.ForeignKey(Persona)
    rol = models.ForeignKey(Rol)
    ACEPTO = "A"
    RECHAZO = "R"
    ESPERA = "E"
    ESTADO_OPCIONES = (
        (ACEPTO, 'Acepto'),
        (RECHAZO,'Rechazo'),
        (ESPERA, 'Espera'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_OPCIONES, default=ESPERA)
    titular = models.BooleanField(default=True)
    observacion = models.TextField(blank=True, null=True)
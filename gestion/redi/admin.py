from advanced_filters.admin import AdminAdvancedFiltersMixin
from django.contrib import admin
from models import *


class PersonaAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    exclude = ['edad']
    list_display = ("nombre", "apellido", "cedula", "email", "numero_contacto", "activa", "edad")
    list_filter = ("activa",)
    advanced_filter_fields = ("nombre", "apellido", "cedula", "email", "numero_contacto", "fecha_nacimiento")


class ActividadAdmin(admin.ModelAdmin):
    raw_id_fields = ("persona",)

# Register your models here.
admin.site.register(Personas, PersonaAdmin)
admin.site.register(Actividades, ActividadAdmin)
admin.site.register(ActividadesTipos)

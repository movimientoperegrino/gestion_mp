from advanced_filters.admin import AdminAdvancedFiltersMixin
from models import *


class PersonaAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    exclude = ['edad']
    list_display = ("nombre", "apellido", "cedula", "email", "numero_contacto", "activa", "edad")
    list_filter = ("activa", "sexo")
    advanced_filter_fields = ("nombre", "apellido", "cedula", "email", "numero_contacto", "fecha_nacimiento", "edad")
    search_fields = ("nombre", "apellido", "cedula", "email", "numero_contacto")



# Register your models here.
admin.site.register(Persona, PersonaAdmin)
admin.site.register(ActividadTipo)

from advanced_filters.admin import AdminAdvancedFiltersMixin
from models import *


class PersonaAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    exclude = ['edad']
    list_display = ("nombre", "apellido", "cedula", "email", "numero_contacto", "activa", "edad")
    list_filter = ("activa","edad")
    advanced_filter_fields = ("nombre", "apellido", "cedula", "email", "numero_contacto", "fecha_nacimiento", "edad")


class ActividadAdmin(admin.ModelAdmin):
    raw_id_fields = ("persona",)

class PlantelXPersonaInline(admin.TabularInline):
    model = PlantelesXPersonas
    raw_id_fields = ("persona","plantel")
    readonly_fields = ["nombre_persona"]

class PlantelAdmin(admin.ModelAdmin):
    inlines = [
        PlantelXPersonaInline,
    ]

# Register your models here.
admin.site.register(Personas, PersonaAdmin)
admin.site.register(Actividades, ActividadAdmin)
admin.site.register(ActividadesTipos)
admin.site.register(Planteles, PlantelAdmin)
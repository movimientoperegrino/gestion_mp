from advanced_filters.admin import AdminAdvancedFiltersMixin
from models import *


class PersonaAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    exclude = ['edad']
    list_display = ("nombre", "apellido", "cedula", "email", "numero_contacto", "activa", "edad")
    list_filter = ("activa", "sexo")
    advanced_filter_fields = ("nombre", "apellido", "cedula", "email", "numero_contacto", "fecha_nacimiento", "edad")
    search_fields = ("nombre", "apellido", "cedula", "email", "numero_contacto")


class ActividadAdmin(admin.ModelAdmin):
    raw_id_fields = ("persona",)


class PlantelXPersonaInline(admin.TabularInline):
    model = PlantelesXPersonas
    raw_id_fields = ("persona", "plantel")
    exclude = ["plantel_x_persona_id",]

class PlantelXPersonaTitularesInline(PlantelXPersonaInline):
    verbose_name_plural = "Titulares"


class PlantelXPersonaSuplentesInline(PlantelXPersonaInline):
    verbose_name_plural = "Suplentes"



class PlantelAdmin(admin.ModelAdmin):
    inlines = [
        PlantelXPersonaTitularesInline, PlantelXPersonaSuplentesInline,
    ]


# Register your models here.
admin.site.register(Personas, PersonaAdmin)
admin.site.register(Actividades, ActividadAdmin)
admin.site.register(ActividadesTipos)
admin.site.register(Planteles, PlantelAdmin)

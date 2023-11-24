from django.contrib import admin
from .models import Profesor

# Register your models here.
class ProfesoresAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","especialidad")
    list_filter=("category",)

admin.site.register(Profesor,ProfesoresAdmin)
# Register your models here.
    
from django.contrib import admin
from .models import User, Patient, info, systematique

# Register your models here.
admin.site.register(User)
admin.site.register(info)
admin.site.register(systematique)
admin.site.site_header='Gestion des dossiers medicaux'
admin.site.site_title='Gestion des dossiers medicaux'

@admin.register(Patient)
class GenericAdmin(admin.ModelAdmin):
    pass
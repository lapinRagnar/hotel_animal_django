from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from hotel_pour_animal.models.personne import Personne
# Register your models here.


@admin.register(Personne)
class PersonneAdmin(ImportExportModelAdmin):
    pass
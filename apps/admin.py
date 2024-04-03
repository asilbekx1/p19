from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.models import Person


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'number', 'photo')
    search_fields = ('first_name',)


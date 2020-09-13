from django.contrib import admin
from .models import Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    fields = (
        'name', 'technology_type',
    )
    list_display = (
        'name', 'technology_type',
    )
    list_filter = ('technology_type', )


from django.contrib import admin
from .models import Startup


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'industry',
                    'development_stage',
                    'prototype_status',
                    'allowed_status',
                    'development_stage',
                    'additional_files',
                    'register_date',
                    'contacts',
                    )
    list_filter = ('name', 'industry', 'development_stage')
    search_fields = ('name', 'industry')
    list_per_page = 20

from django.contrib import admin
from .models import Startup


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'development_stage',)
    list_filter = ('industry', 'development_stage')
    search_fields = ('name', 'industry')
    list_per_page = 20

from django.contrib import admin

from .models import SupportingOrganization


@admin.register(SupportingOrganization)
class SupportingOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'support_type')

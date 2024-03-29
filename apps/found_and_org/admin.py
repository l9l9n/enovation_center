from django.contrib import admin

from .models import SupportingOrganization


@admin.register(SupportingOrganization)
class SupportingOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'support_type',
                    'support_conditions',
                    'additional_files',
                    'contacts',
                    'register_date',
                    )

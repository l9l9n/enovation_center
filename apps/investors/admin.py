from django.contrib import admin

from .models import Investor


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'investment_area',
                    'investment_size',
                    'additional_files',
                    'contacts',
                    'register_date',
                    )

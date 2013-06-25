from django.contrib import admin

from .models import Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = ('alias', 'database_engine', 'database_name', 'database_host', 'database_user', 'database_options')
    list_filter = ('alias', 'database_engine', 'database_host')
    filter_horizontal = (
        'sites',
    )

admin.site.register(Tenant, TenantAdmin)
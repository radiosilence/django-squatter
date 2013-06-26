from django.contrib import admin

from .models import (
    Tenant,
    TenantMapping,
)

class TenantMappingAdmin(admin.ModelAdmin):
    list_display = (
        'site',
        'tenant',
    )
    list_filter = list_display


admin.site.register(TenantMapping, TenantMappingAdmin)


class TenantAdmin(admin.ModelAdmin):
    list_display = (
        'alias',
        'database_engine',
        'database_name',
        'database_host', 
        'database_user', 
    )
    list_filter = (
        'alias',
        'database_engine',
        'database_host',
    )
    filter_horizontal = (
        'sites',
    )
    fieldsets = (
        (None, {
            'fields': ('alias',),
        }),
        ('Database', {
            'fields': (
                'database_engine',
                'database_name',
                'database_host', 
                'database_user', 
                'database_password', 
                'database_options',
            )
        })
    )

admin.site.register(Tenant, TenantAdmin)
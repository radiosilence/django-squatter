from django.contrib import admin

from .models import Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = ('site', 'database_engine', 'database_name', 'database_host', 'database_user', 'database_options')
    list_filter = ('site', 'database_engine', 'database_host')

admin.site.register(Tenant, TenantAdmin)
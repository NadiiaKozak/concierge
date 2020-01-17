# Register your models here.
from django.conf import settings
from django.contrib import admin

from .models import Tenant, Journal, Room


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'phone')
    search_fields = ('first_name', 'last_name', 'phone', 'date_of_birth')
    list_filter = ('date_of_birth', 'last_name')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number_room', 'max_tenants', 'status')
    search_fields = ('number_room', 'max_tenants', 'status')
    list_filter = ('number_room', 'max_tenants', 'status')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'tenant_id', 'tenants', 'key_in', 'key_out')
    search_fields = ('room_id', 'tenant_id', 'tenants', 'key_in', 'key_out')
    list_filter = ('room_id', 'tenant_id', 'tenants', 'key_in', 'key_out')

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from api.models import Client, Contract, Event, EventStatus

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'last_name', 'first_name',
                    'email', 'is_staff', 'group_name')
    search_fields = ['username']

    def group_name(self, obj):
        return obj.groups.values_list('name', flat=True).get()

    group_name.short_description = 'group'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'last_name', 'first_name', 'email', 'phone', 'mobil',
                    'date_created', 'date_updated', 'sales_contact', 'status']
    search_fields = ['last_name', 'email']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['client', 'id', 'sales_contact', 'date_created',
                    'date_updated', 'status', 'amount', 'payment_due']
    search_fields = ['client', 'client__email', 'date_created', 'amount']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['client', 'contract_id', 'event_status', 'date_created', 'date_updated',
                    'support_contact', 'attendees', 'event_date', 'notes']
    search_fields = ['contract_id__client__last_name',
                     'contract_id__client__email', 'event_date']

    def client(self, obj):
        return obj.contract_id.client


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ['status']

from django.contrib import admin

from api.models import Client, Contract, Event

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone', 'mobil',
                    'company_name', 'date_created', 'date_updated', 'sales_contact', 'status']
    list_filter = ('last_name',)
    search_fields = ['last_name']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['sales_contact', 'client', 'date_created',
                    'date_updated', 'status', 'amount', 'payment_due']
    list_filter = ('sales_contact',)
    search_fields = ['sales_contact']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['client', 'date_created', 'date_updated',
                    'support_contact', 'event_status', 'attendees', 'event_date', 'notes']
    list_filter = ('client',)
    search_fields = ['client']

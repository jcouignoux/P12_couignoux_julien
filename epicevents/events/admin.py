from django.contrib import admin

from events.models import Event, EventStatus

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['client', 'contract', 'event_status', 'date_created', 'date_updated',
                    'support_contact', 'attendees', 'event_date', 'notes']
    search_fields = ['client__last_name', 'client__email', 'event_date']

    def client(self, obj):
        return obj.contract.client

    def contract(self, obj):
        return obj.contract


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ['status']

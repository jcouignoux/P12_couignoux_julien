from django.contrib import admin

from events.models import Event, EventStatus

# Register your models here.


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

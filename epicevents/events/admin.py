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

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if request.user.role == 'MA':
                return self.readonly_fields + ('client', 'contract', 'event_status', 'date_created',
                                               'date_updated', 'attendees', 'event_date', 'notes')

        return self.readonly_fields


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ['status']

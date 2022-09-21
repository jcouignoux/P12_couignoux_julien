from django.apps import AppConfig
from events.init import event_status_init


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self):
        event_status_init()

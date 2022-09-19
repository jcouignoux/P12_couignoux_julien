from django.apps import AppConfig
from staff.init import group_init


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff'

    def ready(self):
        pass
        # group_init()

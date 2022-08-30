from django.apps import AppConfig


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff'

    def ready(self):
        from django.contrib.auth.models import Group

        Group.objects.get_or_create(name='Management')
        Group.objects.get_or_create(name='Sales')
        Group.objects.get_or_create(name='Support')

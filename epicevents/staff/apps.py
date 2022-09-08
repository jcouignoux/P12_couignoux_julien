from django.apps import AppConfig


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.contrib.auth.models import Permission

        management = Group.objects.get_or_create(name='Management')[0]
        sales = Group.objects.get_or_create(name='Sales')[0]
        support = Group.objects.get_or_create(name='Support')[0]

        member_view = Permission.objects.get(codename='view_user')
        member_add = Permission.objects.get(codename='add_user')
        member_change = Permission.objects.get(codename='change_user')
        member_delete = Permission.objects.get(codename='delete_user')
        client_view = Permission.objects.get(codename='view_client')
        client_add = Permission.objects.get(codename='add_client')
        client_change = Permission.objects.get(codename='change_client')
        client_delete = Permission.objects.get(codename='delete_client')
        contract_view = Permission.objects.get(codename='view_contract')
        contract_add = Permission.objects.get(codename='add_contract')
        contract_change = Permission.objects.get(codename='change_contract')
        contract_delete = Permission.objects.get(codename='delete_contract')
        event_view = Permission.objects.get(codename='view_event')
        event_add = Permission.objects.get(codename='add_event')
        event_change = Permission.objects.get(codename='change_event')
        event_delete = Permission.objects.get(codename='delete_event')

        managment_permissions = [member_view,
                                 member_add,
                                 member_change,
                                 member_delete,
                                 client_view,
                                 client_change,
                                 contract_view,
                                 contract_change,
                                 event_view,
                                 event_change]
        sales_permissions = [member_view,
                             client_add,
                             client_change,
                             client_delete,
                             client_view,
                             contract_add,
                             contract_change,
                             contract_delete,
                             contract_view,
                             event_add,
                             event_view]
        support_permissions = [member_view,
                               client_view,
                               contract_view,
                               event_add,
                               event_change,
                               event_delete,
                               event_view]

        management.permissions.set(managment_permissions)
        sales.permissions.set(sales_permissions)
        support.permissions.set(support_permissions)

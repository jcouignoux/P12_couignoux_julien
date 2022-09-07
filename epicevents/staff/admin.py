from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission, PermissionsMixin
from django.contrib.auth.models import Group
from django.db import migrations

from staff.models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'last_name', 'first_name',
                    'email', 'is_staff', 'role')
    search_fields = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'last_name', 'first_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
        (None, {'fields': ('role',)}),
        ('Groups', {'fields': ('groups',)}),
    )


admin.site.register(User, UserAdmin)


# class Migration(migrations.Migration):

#     dependencies = [
#         ('authentication', '0001_initial'),
#     ]

#     operations = [
#     ]


# def create_groups(staff, schema_migration):

#     member_view = Permission.objects.get(codename='view_user')
#     member_add = Permission.objects.get(codename='add_user')
#     member_change = Permission.objects.get(codename='change_user')
#     member_delete = Permission.objects.get(codename='delete_user')
#     client_view = Permission.objects.get(codename='view_client')
#     client_add = Permission.objects.get(codename='add_client')
#     client_change = Permission.objects.get(codename='change_client')
#     client_delete = Permission.objects.get(codename='delete_client')
#     contract_view = Permission.objects.get(codename='view_contract')
#     contract_add = Permission.objects.get(codename='add_contract')
#     contract_change = Permission.objects.get(codename='change_contract')
#     contract_delete = Permission.objects.get(codename='delete_contract')
#     event_view = Permission.objects.get(codename='view_event')
#     event_add = Permission.objects.get(codename='add_event')
#     event_change = Permission.objects.get(codename='change_event')
#     event_delete = Permission.objects.get(codename='delete_event')

#     member_write = []
#     managment_permissions = [member_view,
#                              member_add,
#                              member_change,
#                              member_delete,
#                              client_view,
#                              contract_view,
#                              event_view]
#     sale_permissions = [member_view,
#                         client_add,
#                         client_change,
#                         client_delete,
#                         client_view,
#                         contract_add,
#                         contract_change,
#                         contract_delete,
#                         contract_view,
#                         event_add,
#                         event_view]
#     support_permissions = [member_view,
#                            client_view,
#                            contract_view,
#                            event_add,
#                            event_change,
#                            event_delete,
#                            event_view]

#     management = Group.objects.get_or_create(name='Management')
#     sale = Group.objects.get_or_create(name='Sales')
#     support = Group.objects.get_or_create(name='Support')

#     management.permissions.set(managment_permissions)
#     sale.permissions.set(sale_permissions)
#     support.permissions.set(support_permissions)


# class Migration(migrations.Migration):

#     dependencies = [
#         ('authentication', '0001_initial'),
#     ]

#     operations = [
#         migrations.RunPython(create_groups)
#     ]

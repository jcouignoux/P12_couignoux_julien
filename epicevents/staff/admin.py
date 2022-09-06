from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.utils.translation import gettext_lazy as _

from staff.models import User, CustomGroup

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'last_name', 'first_name',
                    'email', 'is_staff', 'group_name')
    search_fields = ['username']

    def group_name(self, obj):
        return obj.groups.values_list('name', flat=True).get()

    group_name.short_description = 'group'


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(CustomGroup)
class GroupAdmin(admin.ModelAdmin):

    list_display = ['group']

    # def permissions(self):
    #     return self.group.permissions


# admin.site.unregister(GroupAdmin)
# admin.site.register(CustomGroup, GroupAdmin)

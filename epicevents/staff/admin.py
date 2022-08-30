from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from staff.models import User

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

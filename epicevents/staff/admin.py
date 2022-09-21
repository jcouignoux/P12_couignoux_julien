from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from staff.models import User
from django.contrib.admin.models import LogEntry

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'last_name', 'first_name',
                    'email', 'is_staff', 'role')
    search_fields = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'last_name', 'first_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (None, {'fields': ('role',)}),
        ('Groups', {'fields': ('groups',)}),
    )
    readonly_fields = ()

    def get_queryset(self, request):
        if request.user.is_superuser:
            queryset = super(UserAdmin, self).get_queryset(request)
        else:
            queryset = User.objects.filter(is_superuser=False)

        return queryset

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if not request.user.is_superuser:
                return self.readonly_fields + ('is_staff', 'is_superuser', 'groups')

        return self.readonly_fields


admin.site.register(User, UserAdmin)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in LogEntry._meta.get_fields()]
    readonly_fields = [f.name for f in LogEntry._meta.get_fields()]

    def get_queryset(self, request):
        if request.user.is_superuser:
            queryset = super(LogEntryAdmin, self).get_queryset(request)
        else:
            queryset = None

        return queryset

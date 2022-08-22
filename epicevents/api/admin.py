from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from api.models import Client, Contract, Event

# Register your models here.


# class GroupInline(admin.TabularInline):
#     model = User.groups.through
#     extra = 0


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'last_name', 'first_name',
                    'email', 'is_staff', 'group_name')

    def group_name(self, obj):
        return obj.groups.values_list('name', flat=True).get()

    group_name.short_description = 'group'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone', 'mobil',
                    'company_name', 'date_created', 'date_updated', 'sales_contact', 'status']
    list_filter = ('last_name',)
    search_fields = ['last_name']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['sales_contact', 'client', 'date_created',
                    'date_updated', 'status', 'amount', 'payment_due']
    list_filter = ('sales_contact',)
    search_fields = ['sales_contact']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['client', 'date_created', 'date_updated',
                    'support_contact', 'event_status', 'attendees', 'event_date', 'notes']
    list_filter = ('client',)
    search_fields = ['client']

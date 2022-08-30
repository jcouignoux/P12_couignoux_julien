from django.contrib import admin

from contracts.models import Contract

# Register your models here.


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['client', 'id', 'sales_contact', 'date_created',
                    'date_updated', 'status', 'amount', 'payment_due']
    search_fields = ['client', 'client__email', 'date_created', 'amount']

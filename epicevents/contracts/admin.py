from django.contrib import admin

from contracts.models import Contract

# Register your models here.


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['client', 'id', 'sales_contact', 'date_created',
                    'date_updated', 'status', 'amount', 'payment_due']
    search_fields = ['client', 'client__email', 'date_created', 'amount']

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if request.user.role == 'MA':
                return self.readonly_fields + ('client', 'id', 'date_created',
                                               'date_updated', 'status', 'amount', 'payment_due', 'event_id')

        return self.readonly_fields

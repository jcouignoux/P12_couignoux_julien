from django.contrib import admin


from clients.models import Client

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'last_name', 'first_name', 'email', 'phone', 'mobil',
                    'date_created', 'date_updated', 'sales_contact', 'status']
    search_fields = ['last_name', 'email']

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if request.user.role == 'MA':
                return self.readonly_fields + ('company_name', 'last_name', 'first_name', 'email', 'phone', 'mobil',
                                               'date_created', 'date_updated', 'status')

        return self.readonly_fields

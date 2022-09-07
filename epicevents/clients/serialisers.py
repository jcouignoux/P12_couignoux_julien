from rest_framework.serializers import ModelSerializer, SerializerMethodField

from clients.models import Client
from contracts.models import Contract
from contracts.serialisers import ContractListSerializer
# from rest_framework.fields import CurrentUserDefault


# class FieldMixin(object):
#     def get_field_names(self, *args, **kwargs):
#         print(self.context['request'].user.role)
#         if self.context['request'].user.role == 'MA':
#             field_names = ['id', 'first_name', 'last_name', 'email',
#                            'company_name', 'sales_contact']
#             extra_kwargs = {
#                 'first_name': {
#                     "required": None,
#                     "read_only": True
#                 }
#             }
#         else:
#             field_names = ['id', 'first_name', 'last_name', 'email',
#                            'company_name', 'sales_contact']
#         if field_names:
#             return field_names

#         return super(FieldMixin, self).get_field_names(*args, **kwargs)


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email',
                  'company_name', 'sales_contact']
        # read_only_fields = ['sales_contact']

    # def get_readonly_fields(self, request, obj=None):
    #     print('toto')
    #     if request.user.role == 'MA':
    #         read_only_fields = ['id', 'first_name', 'last_name', 'email',
    #                             'company_name']
    #     return read_only_fields


class ClientDetailSerializer(ModelSerializer):

    contracts = SerializerMethodField()

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email',
                  'company_name', 'contracts', 'sales_contact']

    def get_contracts(self, instance):
        queryset = Contract.objects.filter(client=instance).all()
        serializer = ContractListSerializer(queryset, many=True)
        return serializer.data

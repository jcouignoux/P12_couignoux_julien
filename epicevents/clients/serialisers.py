from rest_framework.serializers import ModelSerializer, SerializerMethodField

from clients.models import Client
from contracts.models import Contract
from contracts.serialisers import ContractDetailSerializer
# from rest_framework.fields import CurrentUserDefault


class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        if self.context['request'].user.role == 'MA' and self.context['request'].method == 'PUT':
            field_names = ['sales_contact']
        else:
            field_names = ['id', 'first_name', 'last_name', 'email',
                           'company_name', 'sales_contact']
        if field_names:
            return field_names

        return super(FieldMixin, self).get_field_names(*args, **kwargs)


class ClientListSerializer(FieldMixin, ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email',
                  'company_name', 'sales_contact']


class ClientDetailSerializer(ModelSerializer):

    contracts = SerializerMethodField()

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email',
                  'company_name', 'sales_contact', 'contracts']

    def get_contracts(self, instance):
        queryset = Contract.objects.filter(client=instance).all()
        serializer = ContractDetailSerializer(queryset, many=True)
        return serializer.data

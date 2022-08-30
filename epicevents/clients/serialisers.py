from rest_framework.serializers import ModelSerializer, SerializerMethodField

from clients.models import Client


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email',
                  'company_name', 'sales_contact']


class ClientDetailSerializer(ModelSerializer):

    contracts = SerializerMethodField()

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email',
                  'company_name', 'contracts', 'sales_contact']

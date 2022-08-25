from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api.models import Client, Contract, Event


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'groups']


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'groups']


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

    def get_contracts(self, instance):
        queryset = Contract.objects.filter(client=instance)
        serializer = ContractListSerializer(queryset, many=True)
        return serializer.data


class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status']


class ContractDetailSerializer(ModelSerializer):

    event = SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status', 'event']

    def get_event(self, instance):
        queryset = Event.objects.filter(contract_id=instance).first()
        serializer = EventListSerializer(queryset, many=False)
        return serializer.data


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'contract_id',
                  'support_contact', 'event_status', 'notes']


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['event_date', 'support_contact', 'contract_id',
                  'event_status', 'attendees', 'notes']

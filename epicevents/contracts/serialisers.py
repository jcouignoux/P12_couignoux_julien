from rest_framework.serializers import ModelSerializer, SerializerMethodField

from contracts.models import Contract
from events.models import Event
from events.serialisers import EventListSerializer


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

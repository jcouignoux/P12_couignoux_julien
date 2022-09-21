from rest_framework.serializers import ModelSerializer, SerializerMethodField

from contracts.models import Contract
from events.models import Event
from events.serialisers import EventDetailSerializer


class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        if self.context['request'].user.role == 'MA' and self.context['request'].method == 'PUT':
            field_names = ['sales_contact']
        else:
            field_names = ['id', 'sales_contact', 'client',
                           'status', 'amount', 'payment_due']
        if field_names:
            return field_names

        return super(FieldMixin, self).get_field_names(*args, **kwargs)


class ContractListSerializer(FieldMixin, ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client',
                  'status', 'amount', 'payment_due']


class ContractDetailSerializer(ModelSerializer):

    event = SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status', 'event']

    def get_event(self, instance):
        queryset = Event.objects.filter(contract=instance).first()
        serializer = EventDetailSerializer(queryset, many=False)
        return serializer.data

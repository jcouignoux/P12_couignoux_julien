from rest_framework.serializers import ModelSerializer, ValidationError

from events.models import Event
from contracts.models import Contract


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'contract', 'support_contact',
                  'event_status', 'attendees', 'event_date', 'notes']

    # def validate_contract(self, value):
    #     if Contract.objects.filter(id=value.id).first().event_id is not None:
    #         raise ValidationError('Contract already has an event')
    #     return value


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['contract', 'support_contact',
                  'event_status', 'attendees', 'event_date', 'notes']

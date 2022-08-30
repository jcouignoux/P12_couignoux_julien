from rest_framework.serializers import ModelSerializer

from events.models import Event


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

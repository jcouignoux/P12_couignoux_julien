from rest_framework.serializers import ModelSerializer

from events.models import Event


class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        print(self.context['request'].method)
        if self.context['request'].user.role == 'MA' and self.context['request'].method == 'PUT':
            field_names = ['support_contact']
        else:
            field_names = ['id', 'contract', 'support_contact',
                           'event_status', 'attendees', 'event_date', 'notes']
        if field_names:
            return field_names

        return super(FieldMixin, self).get_field_names(*args, **kwargs)


class EventListSerializer(FieldMixin, ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'contract', 'support_contact',
                  'event_status', 'attendees', 'event_date', 'notes']


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['contract', 'support_contact',
                  'event_status', 'attendees', 'event_date', 'notes']

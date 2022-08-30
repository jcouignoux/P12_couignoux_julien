from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from events.serialisers import EventListSerializer, EventDetailSerializer
from staff.permissions import EventPermission
from events.models import Event

# Create your views here.


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class EventViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [EventPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['contract_id__client__last_name',
                        'contract_id__client__email', 'event_date']
    search_fields = ['contract_id__client__last_name',
                     'contract_id__client__email', 'event_date']
    ordering_fields = ['contract_id__client__last_name',
                       'contract_id__client__email', 'event_date']

    def get_queryset(self):

        if 'contract_pk' in self.kwargs:
            queryset = Event.objects.filter(
                contract_id=self.kwargs['contract_pk'])
        else:
            queryset = Event.objects.all()

        return queryset

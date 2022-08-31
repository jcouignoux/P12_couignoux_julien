from django.db import transaction

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status

from events.serialisers import EventListSerializer, EventDetailSerializer
from staff.permissions import EventPermission
from events.models import Event
from contracts.models import Contract

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
    filterset_fields = ['contract__client__last_name',
                        'contract__client__email', 'event_date']
    search_fields = ['contract__client__last_name',
                     'contract__client__email', 'event_date']
    ordering_fields = ['contract__client__last_name',
                       'contract__client__email', 'event_date']

    def get_queryset(self):

        if 'contract_pk' in self.kwargs:
            queryset = Event.objects.filter(
                contract_id=self.kwargs['contract_pk'])
        else:
            queryset = Event.objects.all()

        return queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # contract_id = serializer.data['contract']
        # if Contract.objects.filter(id=contract_id).first().event_id is not None:
        #     return Response({
        #         'event': EventListSerializer(serializer, context=self.get_serializer_context()).data,
        #         'message': "Contract has already an envent."},
        #         status=status.HTTP_304_NOT_MODIFIED)
        # else:
        event = serializer.save()
        contract = event.contract
        contract.status = True
        contract.save()
        return Response({
            'event': EventListSerializer(event, context=self.get_serializer_context()).data,
            'message': "Event created successfully."},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        if event.event_status.status == 'Closed':
            contract = event.client
            contract.status = False
            contract.save()

        return Response({
            'event': EventListSerializer(event, context=self.get_serializer_context()).data,
            'message': "Event created successfully."},
            status=status.HTTP_201_CREATED)

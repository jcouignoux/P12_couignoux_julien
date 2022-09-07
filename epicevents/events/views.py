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
                        'contract__client__email', 'event_date', 'support_contact']
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
        contract = serializer.validated_data.get('contract')
        if contract.event_id == None:
            event = serializer.save()
            contract.status = True
            contract.event_id = event
            contract.save()
            return Response({
                'event': EventListSerializer(event, context=self.get_serializer_context()).data,
                'message': "Event created successfully."},
                status=status.HTTP_201_CREATED)
        else:
            # serializer.contract
            return Response({
                # 'event': EventListSerializer(event, context=self.get_serializer_context()).data,
                'message': "Contract already has an event."},
                status=status.HTTP_409_CONFLICT)

    @ transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance,
                                         data=request.data,
                                         )
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        contract = Contract.objects.filter(id=event.contract.id).first()
        if event.event_status.status == 'CL':
            contract.status = False
        if event.event_status.status == 'OP':
            contract.status = True
        contract.save()

        return Response({
            'event': EventListSerializer(event, context=self.get_serializer_context()).data,
            'message': "Event updated successfully."},
            status=status.HTTP_200_OK)

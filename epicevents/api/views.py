from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.db import transaction, IntegrityError
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Client, Contract, Event
from api.serializers import (UserListSerializer,
                             UserDetailSerializer,
                             ClientListSerializer,
                             ClientDetailSerializer,
                             ContractListSerializer,
                             ContractDetailSerializer,
                             EventListSerializer,
                             EventDetailSerializer)
from api.permissions import MemberPermission, ClientPermission, ContractPermission, EventPermission
# Create your views here.


def index(request):

    return render(request, 'api/index.html')


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class UserViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer
    permission_classes = [MemberPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['username']
    search_fields = ['username']
    ordering_fields = ['username']

    def get_queryset(self):

        return User.objects.filter(is_superuser=False)


class ClientViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [ClientPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['last_name', 'email']
    search_fields = ['last_name', 'email']
    ordering_fields = ['last_name', 'email']

    def get_queryset(self):

        return Client.objects.all()


class ContractViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [ContractPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['client', 'client__email', 'date_created', 'amount']
    search_fields = ['client', 'client__email', 'date_created', 'amount']
    ordering_fields = ['client', 'client__email', 'date_created', 'amount']

    def get_queryset(self):
        print(self.kwargs)
        if 'client_pk' in self.kwargs:
            queryset = Contract.objects.filter(client=self.kwargs['client_pk'])
        else:
            queryset = Contract.objects.all()

        return queryset


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

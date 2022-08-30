from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from contracts.serialisers import ContractListSerializer, ContractDetailSerializer
from staff.permissions import ContractPermission
from contracts.models import Contract
# Create your views here.


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


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

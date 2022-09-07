from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from clients.models import Client
from clients.serialisers import ClientListSerializer, ClientDetailSerializer
from staff.permissions import ClientPermission
# Create your views here.


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ClientViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [ClientPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['last_name', 'email',
                        'company_name', 'status', 'sales_contact']
    search_fields = ['last_name', 'email', 'company_name']
    ordering_fields = ['last_name', 'email', 'company_name']

    def get_queryset(self):

        return Client.objects.all()

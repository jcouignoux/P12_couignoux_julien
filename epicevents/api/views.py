from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.db import transaction, IntegrityError
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from api.models import Client, Contract, Event
from api.serializers import (UserListSerializer,
                             UserDetailSerializer,
                             ClientListSerializer,
                             ClientDetailSerializer,
                             ContractListSerializer,
                             ContractDetailSerializer,
                             EventListSerializer,
                             EventDetailSerializer)
from api.permissions import ManagePermission, SalePermission, SupportPermission
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
    permission_classes = [ManagePermission]

    def get_queryset(self):
        query = ~Q(groups__name='Management')

        return User.objects.filter(query, is_superuser=False)

    # @transaction.atomic
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = User.serializer.save()

    #     return Response({
    #         'project': UserListSerializer(user, context=self.get_serializer_context()).data,
    #         'message': "Member created successfully."},
    #         status=status.HTTP_201_CREATED)


class ClientViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [SalePermission | ManagePermission]

    def get_queryset(self):

        return Client.objects.all()


class ContractViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [SalePermission | ManagePermission]

    def get_queryset(self):

        return Contract.objects.filter(client=self.kwargs['client_pk'])


class EventViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [SalePermission |
                          SupportPermission | ManagePermission]

    def get_queryset(self):

        return Event.objects.filter(contract_id=self.kwargs['contract_pk'])

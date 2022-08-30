
from rest_framework.viewsets import ModelViewSet
from django.db import IntegrityError, transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status

from staff.models import User
from staff.serialisers import UserListSerializer, UserDetailSerializer
from staff.permissions import MemberPermission


# Create your views here.


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

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_staff=True)

        return Response({
            'project': UserListSerializer(user, context=self.get_serializer_context()).data,
            'message': "User created successfully."},
            status=status.HTTP_201_CREATED)

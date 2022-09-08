from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

from rest_framework.viewsets import ModelViewSet
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from staff.models import User
from staff.serialisers import UserListSerializer, UserDetailSerializer, LoginSerializer
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
        group = Group.objects.get(name=user.Name(user.role).label)
        group.user_set.add(user)

        return Response({
            'user': UserListSerializer(user, context=self.get_serializer_context()).data,
            'message': "User created successfully."},
            status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        print(self.request)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_staff=True)
        group = Group.objects.get(name=user.Name(user.role).label)
        group.user_set.add(user)

        return Response({
            'user': UserListSerializer(user, context=self.get_serializer_context()).data,
            'message': "Member updated successfully."},
            status=status.HTTP_200_OK)


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(request, username=username, password=password)

        if user:
            serializer = self.serializer_class(user)
            login(request, user)

            return Response({
                'user': UserListSerializer(user, context=self.get_serializer_context()).data,
                'message': "User logged successfully.",
            },
                status=status.HTTP_200_OK
            )

        return Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)

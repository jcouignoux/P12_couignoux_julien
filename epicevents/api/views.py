from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet


from api.serializers import (UserListSerializer,
                             UserDetailSerializer)
from api.permissions import ManagePermission
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

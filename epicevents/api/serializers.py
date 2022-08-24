from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, SerializerMethodField


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'groups']


class UserDetailSerializer(ModelSerializer):

    issues = SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'groups']

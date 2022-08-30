from rest_framework.serializers import ModelSerializer

from staff.models import User


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'groups']


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'groups']


class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

from rest_framework.serializers import ModelSerializer

from staff.models import User


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'role']


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role']


class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

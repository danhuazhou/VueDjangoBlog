from django.contrib.auth.models import Group, User
# from backend.accounts.models import BlogUser as User
from rest_framework import serializers


class BlogUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = ('url', 'username', 'email', 'groups')
        fields = ('url', 'nickname')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

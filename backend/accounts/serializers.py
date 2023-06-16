from django.contrib.auth.models import Group
from backend.accounts.models import BlogUser as User
from rest_framework import serializers


class BlogUserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name="accounts:user-detail")
    class Meta:
        model = User
        # fields = ('url', 'id','username', 'email', 'groups','nickname')
        fields = ('url', 'nickname', 'username', 'groups')
        extra_kwargs = {'url': {'view_name': 'accounts:user-detail'},
                        'groups': {'view_name': 'accounts:group-detail'}}
        # fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="accounts:group-detail")

    class Meta:
        model = Group
        fields = ('url', 'name')
        # fields = '__all__'

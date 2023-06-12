from django.shortcuts import render
from django.contrib.auth.models import Group
from backend.accounts.models import BlogUser as User
from rest_framework import viewsets
from backend.accounts.serializers import BlogUserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    api
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = BlogUserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    api
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

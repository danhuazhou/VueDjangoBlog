from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Problems
from .serializer import ProblemsSerilalizer


# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'test': reverse('test',request=request,format=format),
            'blogs': reverse('blogs-list',request=request,format=format),
            # 'user-list': reverse('user-list',request=request,format=format),
            # 'user-detail': reverse('user-detail',request=request,format=format),
            'user-detail': reverse('accounts:user-list',request=request,format=format),
        }
    )

class ProblemsViewSet(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerilalizer

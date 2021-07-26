from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from backend.blog.models import Article
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from collections import OrderedDict

from backend.blog.serialize import ArticleSerilalizer
from .models import Article


# Create your views here.

class BlogPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data)
        ]))


class BlogListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    博客列表
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerilalizer
    pagination_class = BlogPagination


class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilalizer
    pagination_class = BlogPagination


def hello(request):
    return HttpResponse("hello")

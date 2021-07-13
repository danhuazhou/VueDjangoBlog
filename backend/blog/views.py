from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from backend.blog.models import Article
from rest_framework.viewsets import ModelViewSet
from backend.blog.serialize import ArticleSerilalizer


# Create your views here.

class BlogPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100


class BlogListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    博客列表
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerilalizer


class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilalizer


def hello(request):
    return HttpResponse("hello")

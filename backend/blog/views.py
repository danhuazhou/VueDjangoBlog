from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class BlogPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100


def hello(request):
    return HttpResponse("hello")

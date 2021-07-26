"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from backend.blog import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from backend.blog.views import BlogListViewSet

router = DefaultRouter()

router.register(r'blogs', BlogListViewSet, basename='blogs')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    url(r'docs/', include_docs_urls(title="my_blog")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('blog/', include('backend.blog.urls', namespace='blog')),
    path('api/666', view=lambda request: HttpResponse('戏说不是胡说')),
    path('accounts/', include('backend.accounts.urls', namespace='accounts')),

]

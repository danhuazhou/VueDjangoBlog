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
from django.urls import path, re_path
from django.http import HttpResponse
from django.views.static import serve
from MyBlog.settings import MEDIA_ROOT
from django.views.generic.base import TemplateView
from backend.blog import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from backend.blog.views import BlogListViewSet
from backend.comments.views import CommentsViewSet
from backend.problems.views import ProblemsViewSet, api_root
from backend.problems.views import MdUploadView
router = DefaultRouter()

router.register(r'blogs', BlogListViewSet, basename='blogs')

router.register(r'comments', CommentsViewSet, basename='comments')
router.register(r'problems', ProblemsViewSet, basename='problems')
# schemas_view = get_schema_view(title='test')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    # path('schema/',schemas_view),
    path('', api_root),
    url(r'api/', include(router.urls)),
    url(r'docs/', include_docs_urls(title="my_blog")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('blog/', include('backend.blog.urls', namespace='blog')),
    path('api/666', view=lambda request: HttpResponse('戏说不是胡说'), name='test'),
    path('accounts/', include('backend.accounts.urls', namespace='accounts')),
    url(r'api/', include('backend.problems.urls', namespace='problems')),
    re_path('^mdeditor/uploads/$', MdUploadView.as_view()),  # 配置编辑器路由
    # path('mdeditor/', include(('mdeditor.urls', 'mdeditor'), namespace='mdeditor')),  # 配置编辑器路由
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),  # 添加上传文件路径
]
from mdeditor import urls
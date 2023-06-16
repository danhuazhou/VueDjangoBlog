from django.conf.urls import url, include
from rest_framework import routers
from backend.accounts import views
from django.urls import path, include

routers = routers.DefaultRouter()
routers.register(r'user', views.UserViewSet, basename='user')
routers.register(r'group', views.GroupViewSet, basename='group')

app_name = 'accounts'

urlpatterns = [
    url(r'^', include(routers.urls)),

]

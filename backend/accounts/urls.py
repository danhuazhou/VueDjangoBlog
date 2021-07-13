from django.conf.urls import url, include
from rest_framework import routers
from backend.accounts import views

routers = routers.DefaultRouter()
routers.register(r'user', views.UserViewSet)
routers.register(r'group', views.GroupViewSet)

app_name = 'accounts'

urlpatterns = [
    url(r'^', include(routers.urls)),

]

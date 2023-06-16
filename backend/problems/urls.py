from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.conf.urls import url, include
from rest_framework import routers
router = DefaultRouter()
router.register('problems', views.ProblemsViewSet, basename='problems')

app_name = 'problems'
urlpatterns = [
    url(r'^', include(router.urls)),

]
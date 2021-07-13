from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register('user', views.Article, basename='user')

app_name = 'blog'

urlpatterns = [
    path('', views.hello)

]

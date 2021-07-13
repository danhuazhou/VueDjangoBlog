from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from rest_framework import viewsets


# Create your models here.

class BlogUser(AbstractUser):
    nickname = models.CharField('昵称', max_length=100, blank=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('最后修改', default=now)
    source = models.CharField('来源', max_length=100, blank=True)


# class BlogUserViewSet(viewsets.ModelViewSet):
#     """
#     pass
#     """
#     pass

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.urls import reverse
import uuid
from MyBlog.utils import get_current_site
from rest_framework import viewsets


# Create your models here.

class BlogUser(AbstractUser):
    nickname = models.CharField('昵称', max_length=100, blank=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('最后修改', default=now)
    source = models.CharField('来源', max_length=100, blank=True)
    uid = models.UUIDField('身份标识', default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('blog:author_detail',
                       kwargs={'author_name': self.username})

    def get_full_url(self):
        site = get_current_site().domain
        url = "https://{site}{path}".format(site=site,
                                            path=self.get_absolute_url())
        return url

    class Meta:
        ordering = ('-username', '-date_joined',)
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
        db_table = 'accounts_users'
# class BlogUserViewSet(viewsets.ModelViewSet):
#     """
#     pass
#     """
#     pass

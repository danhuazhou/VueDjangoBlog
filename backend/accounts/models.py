from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.

class BlogUser(AbstractUser):
    nickname = models.CharField('', max_length=100, blank=True)
    created_time = models.DateTimeField('', default=now)
    last_mod_time = models.DateTimeField('', default=now)
    source = models.CharField('', max_length=100, blank=True)



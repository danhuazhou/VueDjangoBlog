from django.contrib import admin
from .models import BlogUser


# Register your models here.

class BlogUserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'created_time', 'last_mod_time', 'source']


admin.site.register(BlogUser, BlogUserAdmin)

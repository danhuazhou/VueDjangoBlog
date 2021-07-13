from django.contrib import admin
from .models import Article, Category, Tag


# Register your models here.

class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "type")


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_category", "slug")


@admin.register(Tag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Article, BlogArticleAdmin)
admin.site.register(Category, BlogCategoryAdmin)

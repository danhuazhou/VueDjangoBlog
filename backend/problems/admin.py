from django.contrib import admin
from .models import Problems, Tag, Category


# Register your models here.

class ProblemsAdmin(admin.ModelAdmin):
    list_display = ("title",)


class ProblemsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_category", "slug")


@admin.register(Tag)
class ProblemsTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Category, ProblemsCategoryAdmin)

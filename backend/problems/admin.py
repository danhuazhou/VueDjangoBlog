from django.contrib import admin
from django.utils.html import format_html
from .models import Problems, Tag, Category


# Register your models here.

class ProblemsAdmin(admin.ModelAdmin):
    list_display = (
        "title", "difficulty_", "category", "emphasis", "passing_rate",
        "review_time", "redirect_url")
    search_fields = ("title",)
    list_filter = ("difficulty", "category", "website")
    ordering = ('-id', '-review_time')

    def passing_rate(self, obj):
        s = int(obj.successes) if obj.successes else 0
        f = int(obj.failtures) if obj.failtures else 0
        if (s + f) != 0:
            return format(s / (s + f), '.2%')
        else:
            return format(0, '.2%')

    def redirect_url(self, obj):
        if obj.url:
            return format_html('<a href="{0}" target="_blank">题目链接</a>',
                               obj.url)
        else:
            return '-'

    redirect_url.short_description = '跳转链接'
    passing_rate.short_description = "通过率"


class ProblemsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_category", "slug")


@admin.register(Tag)
class ProblemsTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Category, ProblemsCategoryAdmin)

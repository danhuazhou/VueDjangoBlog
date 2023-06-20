from django.contrib import admin
from .models import Problems, Tag, Category


# Register your models here.

class ProblemsAdmin(admin.ModelAdmin):
    list_display = ("title", "difficulty", "emphasis", "passing_rate", "url")
    search_fields = ("title",)

    def passing_rate(self, obj):
        s = int(obj.successes) if obj.successes else 0
        f = int(obj.failtures) if obj.failtures else 0
        if (s + f) != 0:
            return format(s / (s + f), '.2%')
        else:
            return format(0, '.2%')

    passing_rate.short_description = "通过率"


class ProblemsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_category", "slug")


@admin.register(Tag)
class ProblemsTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Category, ProblemsCategoryAdmin)

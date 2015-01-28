from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
import models


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created", "publish")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "mature")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Category)
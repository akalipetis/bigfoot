from django.contrib import admin

from . import models


class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 1


admin.site.register(models.Sighting, inlines=[CommentInline])


# Register your models here.
admin.site.register(models.User)

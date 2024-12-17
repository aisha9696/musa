from django.contrib import admin
from webapp import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_publishing', 'author', 'description')


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'dates_of_life', 'biography')


admin.site.register(models.Genre)



from django.contrib import admin
from webapp import models


# admin.site.register(models.Articles)
@admin.register(models.Record)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'status', 'created_at')
    list_editable = ('author', 'email', 'status')
    list_filter = ('author', 'created_at')
    search_fields = ('author', 'text')
    fields = ('email', 'author', 'text', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'date', 'is_active', 'count_view')
    list_filter = ('date', 'is_active')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}




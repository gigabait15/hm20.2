from django.contrib import admin

from main.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name_version', 'active_version')
    list_filter = ('name_version',)
    search_fields = ('number_version', 'name_version',)
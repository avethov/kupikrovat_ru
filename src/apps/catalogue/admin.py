from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'date_updated']
    ordering = ['name']
    actions = ['make_published', 'make_withdrawn']

    def make_published(self, request, queryset):
        queryset.update(status='p')

    def make_withdrawn(self, request, queryset):
        queryset.update(status='w')

    make_published.short_description = u"Опубликовать выделенные товары"
    make_withdrawn.short_description = u"Изъять выделенные товары"

admin.site.register(Product)

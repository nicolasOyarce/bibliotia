from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'editorial', 'price', 'stock', 'is_available')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Product, ProductAdmin)
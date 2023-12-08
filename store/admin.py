from django.contrib import admin

from .models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'editorial', 'price', 'stock', 'is_available')
    prepopulated_fields = {'slug': ('title', )}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active', )

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
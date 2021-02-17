from django.contrib import admin
from .models import Product, Category, Colour, Occasion


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'colour',
        'occasion',
        'popular',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)

class ColourAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)

class OccasionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Occasion, OccasionAdmin)

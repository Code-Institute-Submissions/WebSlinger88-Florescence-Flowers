from django.contrib import admin
from .models import (
    Product, Category, Colour, Occasion, ProductReview, ProductRating)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'colour',
        'occasion',
        'popular',
        'avg_rating',
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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'content',
        'user',
        'id',
    )


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'rating',
        'review',
        'id',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Occasion, OccasionAdmin)
admin.site.register(ProductReview, ReviewAdmin)
admin.site.register(ProductRating, RatingAdmin)

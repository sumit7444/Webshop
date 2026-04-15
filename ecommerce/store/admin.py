from django.contrib import admin
from .models import Category, Product, ProductImage, Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('user', 'rating', 'comment', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount_price', 'stock', 'available', 'featured']
    list_filter = ['available', 'featured', 'category']
    list_editable = ['price', 'stock', 'available', 'featured']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ReviewInline]
    search_fields = ['name', 'description']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['rating']

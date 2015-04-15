from django.contrib import admin

from mainapp.models import Article, Product, ArticleImage, ProductImage, Image

# Register your models here.

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage


class ArticleAdmin(admin.ModelAdmin):
        inlines = [ArticleImageInline, ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
        inlines = [ProductImageInline, ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Category, Size, Product
from .models import ProductImage , ProductSize


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'color', 'price']
    list_filter = ['category', 'color']
    search_fields = ['name', 'color', 'decription'] 
    prepolated_fileds = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSizeInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepolated_fileds = {'slug': ('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)
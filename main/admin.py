from django.contrib import admin

# Register your models here.
from .models import Tag, ProductGroup, Product, Shop, Purchase


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "created_by"
    list_display_links = "pk", "name"


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    def tags_output(self, obj):
        tags = [tag.name for  tag in obj.tags.all()]
        return tags
    list_display = "pk", "name", "tags_output", "description", "created_by"
    list_display_links = "pk", "name"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "group"
    list_display_links = "pk", "name"


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "created_by"
    list_display_links = "pk", "name"


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    def date_output(self, obj):
        return obj.date.strftime("%Y-%m-%d")

    date_output.admin_order_field = 'date'
    date_output.short_description = 'Date output'
    list_display = "pk", "date_output", "product","quantity", "total", "shop", "user"
    list_display_links = "pk", "product"





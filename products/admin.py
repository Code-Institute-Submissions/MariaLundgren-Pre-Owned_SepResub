from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'color',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

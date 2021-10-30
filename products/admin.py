from django.contrib import admin
from .models import Product, Category

# Register your models here.

# Below is a tuple change the list order below to change order in which they 
# are displayed on the site
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)
    # To reverse the order put a - infront of sku

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

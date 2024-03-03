from django.contrib import admin
from .models import Client, Product, ProductImage, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_date']
    list_filter = ['registration_date']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    fieldsets = [
        ('Клиент', {'fields': ['name', 'registration_date']}),
        ('Контактная информация', {'fields': ['email', 'phone', 'address']}),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по бренду'
    list_filter = ['price']
    fieldsets = [
        ('Модель', {'fields': ['name', 'price']}),
        ('Описание', {'fields': ['description'], 'classes': ['collapse']}),
        ('Доп.информация', {'fields': ['product_count', 'added_at']}),
    ]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'image']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'created_at']
    list_filter = ['total_price']
    search_fields = ['created_at']
    search_help_text = 'Поиск по дате'
    fieldsets = [
        ('Заказ', {'fields': ['products', 'total_price', 'created_at']}),
        ('Заказчик', {'fields': ['client']}),
    ]

from django.contrib import admin

from fastfood.models import CustomUser, FoodMeny, Order, OrderItem


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'role']
    list_display_links = ['username']
    list_filter = ['role', ]


@admin.register(FoodMeny)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'price', "is_available"]
    list_display_links = ['id', 'name']
    search_fields = ['name', ]
    list_filter = ['is_available', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_foods', 'delivery_time', 'created_at']
    list_filter = ['created_at', ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'food', 'quantity']
    list_display_links = ['id', ]

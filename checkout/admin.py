from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total')

    list_display = ('order_number', 'date', 'name', 'total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

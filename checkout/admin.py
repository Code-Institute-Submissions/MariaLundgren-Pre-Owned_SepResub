from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total')

    list_display = ('order_number', 'date', 'name', 'total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

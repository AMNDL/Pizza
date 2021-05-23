import admin_thumbnails
from django.contrib import admin
from .models import Pizza, Order


class OrderInline(admin.TabularInline):
    extra = 0
    model = Order.pizzas.through
    verbose_name = 'Пиццы в заказе'
    verbose_name_plural = 'Пиццы в  заказе'


@admin.register(Pizza)
@admin_thumbnails.thumbnail('image')
class PizzaAdmin(admin.ModelAdmin):
    inlines = [OrderInline, ]
    list_display = ['name', 'price', 'image_thumbnail']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'customer_name', 'delivery_time', 'price')

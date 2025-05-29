from django.contrib import admin
from stocks.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'images_0', 'images_1', 'images_2', 'images_3', 'price', 'quantity', 'variations')

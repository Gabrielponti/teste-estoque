from django.contrib import admin
from color.models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_color')
    search_fields = ('name_color',)

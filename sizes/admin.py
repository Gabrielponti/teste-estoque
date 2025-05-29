from django.contrib import admin
from .models import Size


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')
    search_fields = ('size',)

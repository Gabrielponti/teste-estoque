from django.contrib import admin
from number.models import Number

# Register your models here.
@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_number')
    search_fields = ('name_number',)
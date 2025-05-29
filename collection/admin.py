from django.contrib import admin
from collection.models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_collection')
    search_fields = ('name_collection',)

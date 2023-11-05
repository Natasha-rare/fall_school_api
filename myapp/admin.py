from django.contrib import admin
from . import models

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'is_active', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'description')
    list_display_links = ('id', 'name')

admin.site.register(models.Item, ItemAdmin)
from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'priority', 'created_at']
    list_filter = ['category', 'priority', 'created_at']
    search_fields = ['title', 'description']

from django.contrib import admin
from .models import DataHistory


@admin.register(DataHistory)
class DataHistoryAdmin(admin.ModelAdmin):
    list_display = ("api_type", "timestamp")

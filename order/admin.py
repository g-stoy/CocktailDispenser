from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "machine", "recipe", "created_at")
    list_filter = ("machine", "recipe")
    date_hierarchy = "created_at"


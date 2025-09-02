from django.contrib import admin
from .models import Machine, BottleSlot, MachineIssue

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "store",)
    list_filter = ("store",)
    search_fields = ("serial_number",)

@admin.register(BottleSlot)
class BottleSlotAdmin(admin.ModelAdmin):
    list_display = ("machine", "position", "ingredient")
    list_filter = ("machine",)

@admin.register(MachineIssue)
class MachineIssueAdmin(admin.ModelAdmin):
    list_display = ("title", "machine", "severity", "is_resolved", "created_at", "resolved_at")
    list_filter = ("severity", "is_resolved", "machine")
    search_fields = ("title", "description")

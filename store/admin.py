from django.contrib import admin
from .models import Store, StoreRentPayment

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "created_at", "rent_amount", "next_due_date", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "location")


@admin.register(StoreRentPayment)
class StoreRentPaymentAdmin(admin.ModelAdmin):
    list_display = ("store", "amount", "due_date")
    list_filter = ("store",)


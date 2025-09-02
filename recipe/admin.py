from django.contrib import admin
from .models import Ingredient, Recipe, RecipeSlot

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)

class RecipeSlotInline(admin.TabularInline):
    model = RecipeSlot
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    inlines = [RecipeSlotInline]


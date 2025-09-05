from rest_framework import serializers
from .models import Machine, BottleSlot
from recipe.models import Recipe, RecipeSlot, Ingredient
from store.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["id", "name", "location"]

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "category", "is_carbonated"]


class BottleSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = BottleSlot
        fields = ["position", "ingredient", "quantity_ml", "capacity_ml", "last_refilled"]

class RecipeSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeSlot
        fields = ["slot_number", "ingredient", "amount_ml"]

class RecipeSerializer(serializers.ModelSerializer):
    slots = RecipeSlotSerializer(many=True, read_only=True) 

    class Meta:
        model = Recipe
        fields = ["id", "name", "description", "is_active", "slots"]

class MachineSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    bottle_slots = BottleSlotSerializer(many=True, read_only=True)

    class Meta:
        model = Machine
        fields = ["id", "serial_number", "slots", "store", "bottle_slots"]

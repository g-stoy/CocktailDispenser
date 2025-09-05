from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializer, RecipeSerializer, IngredientSerializer
from recipe.models import Recipe, RecipeSlot, Ingredient

@api_view(["GET"])
def sync_machine(request, serial_number):
    try:
        machine = Machine.objects.prefetch_related("bottle_slots").select_related("store").get(serial_number=serial_number)
    except Machine.DoesNotExist:
        return Response({"error": "Machine not found"}, status=status.HTTP_404_NOT_FOUND)

    machine_data = MachineSerializer(machine).data

    slot_ingredients_ids = machine.bottle_slots.values_list("ingredient__id", flat=True)
    ingredients = IngredientSerializer(Ingredient.objects.filter(id__in=slot_ingredients_ids), many=True).data

    recipes_ids = RecipeSlot.objects.filter(ingredient__in=slot_ingredients_ids).values_list("recipe__id", flat=True).distinct()
    recipes = RecipeSerializer(Recipe.objects.filter(id__in=recipes_ids).prefetch_related("slots"), many=True).data

    data = {
        "machine": machine_data,
        "ingredients": ingredients,
        "recipes": recipes
    }

    return Response(data, status=status.HTTP_200_OK)

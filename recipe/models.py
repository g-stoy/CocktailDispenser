from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    is_carbonated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RecipeSlot(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="slots")
    slot_number = models.PositiveIntegerField()
    amount_ml = models.PositiveIntegerField() 
    
    def __str__(self):
        return f"{self.ingredient.name} ({self.amount_ml}ml)"
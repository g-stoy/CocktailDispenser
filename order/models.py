from django.db import models
from recipe.models import Recipe
from machine.models import Machine

class Order(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="orders")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.recipe.name}"

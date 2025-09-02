from django.db import models

from store.models import Store
from recipe.models import Ingredient

class Machine(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="machines")
    serial_number = models.CharField(max_length=255)
    slots = models.PositiveIntegerField(default=5)  # Number of bottle slots

    def __str__(self):
        return f"{self.name} ({self.store.name})"


class BottleSlot(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="bottle_slots")
    position = models.PositiveIntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_ml = models.PositiveIntegerField(default=0) 
    capacity_ml = models.PositiveIntegerField(default=1000) 
    last_refilled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Slot {self.position} - {self.machine.name}"

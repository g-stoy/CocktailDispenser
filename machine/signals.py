from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Machine, BottleSlot

@receiver(post_save, sender=Machine)
def create_bottle_slots(sender, instance, created, **kwargs):
    if created:
        for pos in range(1, instance.slots + 1):
            BottleSlot.objects.create(machine=instance, position=pos)
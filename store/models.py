from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    next_due_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({'Active' if self.is_active else 'Inactive'})"


class StoreRentPayment(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.store.name} - {self.amount} ({'Paid' if self.paid else 'Pending'})"

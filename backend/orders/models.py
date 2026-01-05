from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.amount})"

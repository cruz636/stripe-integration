from django.db import models
from django.db.models.base import Model

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="365 Item.")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stripe_url = models.CharField(default="No payment link.", max_length=250)

    def __str__(self) -> str:
        return self.name

    def get_stripe_payment_link(self):
        # TODO
        return 0

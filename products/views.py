from django.db import models

# Create your views here.

class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory_quantity = models.IntegerField()



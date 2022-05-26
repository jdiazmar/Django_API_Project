from django.db import models

# Create your views here.

class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_length=2)
    inventory_quantity = models.IntegerField(max_length=8)

    

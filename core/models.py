from django.db import models
import uuid
from decimal import Decimal
# Create your models here.

class Restaurant(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=14)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    

class Food(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    restaurant = models.ForeignKey("core.Restaurant", on_delete=models.CASCADE)
    food_type = models.ForeignKey("core.FoodType", on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    caption = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class FoodType(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    restaurant = models.ForeignKey("core.Restaurant", on_delete=models.CASCADE)
    
    type = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.type

class Order(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    restaurant = models.ForeignKey("core.Restaurant", on_delete=models.CASCADE)
    cart = models.ManyToManyField("core.Food")
    price = models.DecimalField(max_digits=5, decimal_places=3)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def final_price(self) -> Decimal:
        final : Decimal = Decimal(0)

        for food in self.cart.all():
            final += food.price
        
        return final

    def __str__(self):
        return self.created_at

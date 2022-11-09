from django.contrib import admin
from .models import *

# Register your models here.

admin.register(Restaurant)
admin.register(Food)
admin.register(FoodType)
admin.register(Order)
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(FoodType)
admin.site.register(Order)
from time import time
from django import template
from users.models import CustomUser
from core.models import *
import html
from django.utils import timezone
register = template.Library()



def food_type_user(food_type, user):
    return food_type.food_set.filter(restaurant__name=user.restaurant)


register.filter('food_type_user', food_type_user)

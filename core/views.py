from django.shortcuts import redirect, render
from django.contrib import messages
from users.models import CustomUser
from .models import *
from .forms import *
# Create your views here.


def home(request):
    user = CustomUser.objects.get(id=request.user.id)
    food = Food.objects.filter(restaurant=user.restaurant)
    food_types = FoodType.objects.filter(restaurant=user.restaurant)
    context = {
        'user':user,
        '_food':food,
        'food_types':food_types,
    }

    return render(request, 'home.html', context)


def add_food_type(request):
    user = CustomUser.objects.get(id=request.user.id)

    if request.method == "POST":
        form = FoodTypeForm(request.POST)
        if form.is_valid():
            _type = form.save(commit=False)
            _type.restaurant = user.restaurant
            _type.save()
            messages.success(request, f"{_type.name} has been added succesfully!")
            return redirect('home')
            
    else:
        form = FoodTypeForm()
    
    context = {
        "user":user,
        'form':form
    }

    return render(request, 'add_food_type.html', context)

def edit_food_type(request, type_id):
    user = CustomUser.objects.get(id=request.user.id)
    _type = FoodType.objects.get(id=type_id)
    if request.method == "POST":
        form = FoodTypeForm(request.POST, instance = _type)
        if form.is_valid():
            _type = form.save(commit=False)
            _type.restaurant = user.restaurant
            _type.save()
            messages.success(request, f"{_type.name} has been edited succesfully!")
            return redirect('home')
    else:
        form = FoodTypeForm(instance = _type)
    
    context = {
        "user":user,
        'form':form
    }

    return render(request, 'edit_food_type.html', context)

def delete_food_type(request, type_id):
    _type = FoodType.objects.get(id=type_id)
    messages.warning(request, f"{_type.type} has been deleted")
    _type.delete()
    return redirect("home")


def add_food(request):
    user = CustomUser.objects.get(id=request.user.id)

    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            _food = form.save(commit=False)
            _food.restaurant = user.restaurant
            _food.save()
            messages.success(
                request, f"{_food.name} has been added succesfully!")
            return redirect('home')

    else:
        form = FoodForm()

    context = {
        "user": user,
        'form': form
    }

    return render(request, 'add_food.html', context)


def edit_food(request, type_id):
    user = CustomUser.objects.get(id=request.user.id)
    _food = FoodType.objects.get(id=type_id)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=_food)
        if form.is_valid():
            _food = form.save(commit=False)
            _food.restaurant = user.restaurant
            _food.save()
            messages.success(
                request, f"{_food.name} has been edited succesfully!")
            return redirect('home')
    else:
        form = FoodForm(instance=_food)

    context = {
        "user": user,
        'form': form
    }

    return render(request, 'edit_food.html', context)


def delete_food(request, food_id):
    """
        Deletes Food
    """
    food = Food.objects.get(id=food_id)
    messages.warning(request, f"{food.name} has been deleted")
    food.delete()
    return redirect("home")

def add_food_cart(request):
    """
        Adds FoodCart item to Cart
    """

    user = CustomUser.objects.get(id=request.user.id)

    cart, created = Cart.objects.get_or_create(
        restaurant__name = user.restaurant
    )

    if request.method == "POST":
        form = FoodCartForm(request.POST)
        if form.is_valid():
            food_cart = form.save(commit=False)
            food_cart.restaurant = user.restaurant
            food_cart.description = user.description
            food_cart.save()
            cart.cart.add(food_cart)
            messages.success(
                request, f"{food_cart.food.name} has been added succesfully!")
            return redirect('home')

    else:
        form = FoodCartForm()

    context = {
        "user": user,
        'form': form
    }

    return render(request, 'add_food.html', context)


def delete_food_cart(request, food_cart_id):
    """
        Deletes FoodCart item from Cart
    """
    food_cart = FoodCart.objects.get(id=food_cart_id)
    messages.warning(request, f"{food_cart.type} has been deleted")
    food_cart.delete()
    return redirect("home")

def add_order(request):
    """
        Copies FoodCart items from Cart to Order and resets Order
    """
    user = CustomUser.objects.get(id=request.user.id)

    cart, created = Cart.objects.get_or_create(
        restaurant__name=user.restaurant
    )
    order = Order.objects.create(
        restaurant = user.restaurant
    )

    order.save()

    for food_cart in cart.cart.all():
        order.cart.add(food_cart)
        order.price += food_cart.food.price
    
    order.save()

    cart.price = Decimal(0)
    cart.cart.all().delete()
    cart.save()

    messages.success(request, "Order was successful")
    return redirect('home')


def list_orders(request):
    user = CustomUser.objects.get(id=request.user.id)
    orders = Order.objects.filter(restaurant__name=user.restaurant).order_by("-created_at")

    context = {
        'user':user,
        'orders': orders
    }

    return render(request, 'orders.html', context)


def generate_order_reciept(request, order_id):
    """
        Generates PDF Reciept of One Order
    """
    
    user = CustomUser.objects.get(id=request.user.id)
    order = Order.objects.get(
        id=order_id)


def generate_all_order_reciept(request):
    """
        Generates PDF Reciept of One Order
    """
    
    user = CustomUser.objects.get(id=request.user.id)
    orders = Order.objects.filter(
        restaurant__name=user.restaurant).order_by("-created_at")


from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('type/add', views.add_food_type, name='add_food_type'),
    path('type/delete/<str:type_id>', views.add_food_type, name='add_food_type'),

    path('food/add', views.add_food, name='add_food'),
    path('food/delete/<str:food_id>', views.delete_food, name='delete_food'),
    path('food/edit/<str:food_id>', views.edit_food, name='edit_food'),

    path('cart/add', views.add_food_cart, name='add_food_cart'),
    path('cart/delete/<str:food_cart_id>',
         views.delete_food_cart, name='delete_food_cart'),

    path('checkout', views.add_order, name='checkout'),
    path('orders', views.list_orders, name='orders'),
    path('orders/reciept', views.generate_all_order_reciept,
         name='generate_all_order_reciept'),
    path('orders/reciept/<str:order_id>',
         views.generate_order_reciept, name='generate_order_reciept'),

] 

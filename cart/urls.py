from django.urls import path
from .views import *
urlpatterns = [
    path('cart_item/<int:id>/',add_to_cart,name='add_to_cart'),
    path('cart_view/',cart_view,name='cart_view'),
    path('item_increase/<int:id>/',item_increase,name='item_increase'),
    path('item_decrease/<int:id>/',item_decrease,name='item_decrease'),
    path('item_remove/<int:id>/',item_remove,name='item_remove'),
]

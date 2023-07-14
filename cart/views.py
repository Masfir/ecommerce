from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from store.models import *
from django.contrib import messages
# Create your views here.

def add_to_cart(request,id):
    item = get_object_or_404(Product,id=id)
    item_cart = Cart.objects.get_or_create(cart_item=item,user=request.user,purchased=False)
    item_order = Order.objects.filter(user=request.user,ordered=False)
    print(item_order)
    if item_order.exists():
        orders = item_order[0]
        if orders.order_items.filter(cart_item=item,user = request.user).exists():
            item_cart[0].quantity += 1
            item_cart[0].save()
            messages.success(request,"Item successfully updated")
            return redirect('/')
        else:
            orders.order_items.add(item_cart[0])
            messages.success(request,"Item successfully added")
            return redirect('/')
           

    else:
        order = Order(user=request.user,ordered=False)
        order.save()
        order.order_items.add(item_cart[0])
        messages.success(request,"Item successfully added")
        return redirect('/')

def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    oreders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and oreders.exists():
        oreder = oreders[0]
        context ={
            'carts':carts,
            'oreder':oreder,
        }
        return render(request,'cart/cart_view.html',context)
    else:
        return redirect('/')

def item_remove(request,id):
    item = get_object_or_404(Product,id=id)
    order = Order.objects.filter(user = request.user,ordered=False)
    if order.exists():
        order = order[0]
        if order.order_items.filter(cart_item=item,purchased=False).exists():
            cart = Cart.objects.filter(cart_item=item,purchased=False,user=request.user)[0]
            order.order_items.remove(cart)
            cart.delete()
            messages.warning(request,"Successfully remove")
            return redirect('cart_view')


def item_increase(request,id):
    item = get_object_or_404(Product,id=id)
    order = Order.objects.filter(user = request.user,ordered=False)
    if order.exists():
        order = order[0]
        if order.order_items.filter(cart_item=item,purchased=False).exists():
            cart = Cart.objects.filter(cart_item=item,purchased=False,user=request.user)[0]
            cart.quantity += 1
            cart.save()
            return redirect('cart_view')
        

def item_decrease(request,id):
    item = get_object_or_404(Product,id=id)
    order = Order.objects.filter(user = request.user,ordered=False)
    if order.exists():
        order = order[0]
        if order.order_items.filter(cart_item=item,purchased=False).exists():
            cart = Cart.objects.filter(cart_item=item,purchased=False,user=request.user)[0]
            cart.quantity -= 1
            cart.save()
            return redirect('cart_view')
        






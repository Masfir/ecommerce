from django import template
from cart.models import Cart,Order

register = template.Library()

@register.filter
def cart_item_count(user):
    count_qs = Cart.objects.filter(user=user,purchased=False)
    return count_qs.count()

@register.filter
def cart_item_info(user):
    item_info = Cart.objects.filter(user=user,purchased=False)
    return item_info

@register.filter
def total_order_price(user):
    total_price = Order.objects.filter(user=user,ordered=False)
    if total_price.exists():
        return total_price[0].get_order_price_total()
    else:
        return 0
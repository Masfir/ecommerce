from django.db import models
from django.contrib.auth.models import User
from store.models import *
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart')
    cart_item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def get_cart_total(self):
        total = self.quantity * self.cart_item.price
        float_total = format(total,'0.2f')
        return float_total
    
    def __str__(self) -> str:
        return f'{self.cart_item.name}--{self.quantity } x {self.cart_item.price}'
    

class Order(models.Model):
    PAYMENT_METHOD =(
        ('Cash On Delivary','Cash On Delivary'),
        ('SSLCommerze','SSLCommerze'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order')
    order_items = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    orderId = models.CharField(max_length=30,blank=True,null=True)
    paymentId = models.CharField(max_length=30,blank=True,null=True)
    payment_method = models.CharField(max_length=26,choices=PAYMENT_METHOD,default='Cash On Delivary')
    created = models.DateTimeField(auto_now_add=True)

    def get_order_price_total(self):
        total = 0
        for cart_item in self.order_items.all():
            total += float(cart_item.get_cart_total())
        return total

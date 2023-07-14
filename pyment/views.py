from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BillingAdressForm,OrderForm
from .models import BillingAdress
from cart.models import Cart,Order
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#SSLCommerze integration
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket




def checkout(request):
    billing_address = BillingAdress.objects.get_or_create(user=request.user)
    billing_address = billing_address[0]
    billing_form = BillingAdressForm(instance=billing_address)
    order_form = OrderForm()

    order_qs = Order.objects.filter(user=request.user,ordered=False)[0]
    order_item = order_qs.order_items.count()
    order_item_name = order_qs.order_items.all()
    total_amount = order_qs.get_order_price_total()
    print(total_amount)


    if request.method == 'POST' or request.method == 'post':
        billing_address = BillingAdress.objects.get_or_create(user=request.user)[0]
        billing_form = BillingAdressForm(request.POST,instance=billing_address)
        order_form = OrderForm(request.POST,instance=order_qs)
        print(billing_form)
        # print(order_form)

        # if not billing_address.is_fully_filled():
        #     return redirect('checkout')
    

        if billing_form.is_valid() and order_form.is_valid():
            billing_form.save()
            payment_form = order_form.save(commit=False)

            if payment_form.payment_method == 'Cash On Delivary':
                
                order_qs.ordered = True
                order_qs.paymentId = payment_form.payment_method
                order_qs.orderId = get_random_string(10)
                order_qs.save()
                cart_qs = Cart.objects.filter(user=request.user,purchased=False)
                for item in cart_qs:
                    item.purchased = True
                    item.save()
                return redirect('/')
            
            if payment_form.payment_method == 'SSLCommerze':
                store_id = 'abc626e225657a3c'
                API_key = 'abc626e225657a3c@ssl'
                mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)

                status_url = request.build_absolute_uri(reverse('complete'))

                mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

                mypayment.set_product_integration(total_amount=total_amount, currency='BDT', product_category='None', product_name=order_item_name, num_of_item=order_item, shipping_method='NO', product_profile='None')
                
                current_user = request.user
                print(current_user.username,"current_user")
                # print(current_user.user_pro.full_name,"current_user")
                mypayment.set_customer_info(name=current_user.username, email=current_user.email, address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')

                mypayment.set_shipping_info(shipping_to=billing_address.first_name, address=billing_address.address, city=billing_address.city, postcode='1209', country='Bangladesh')
                order_qs.payment_method = payment_form.payment_method
                response_data = mypayment.init_payment()
                return redirect(response_data['GatewayPageURL'])





    context = {
        'billing_form':billing_form,
        'order_form':order_form,
        'total_amount':total_amount,
    }


    return render(request,"payment/checkout_page.html",context)

@csrf_exempt
def complete(request):
    print(request.POST)
    if request.method =='POST' or request.method =='post':
        status = request.POST['status']
        if status == 'VALID':
            tran_id = request.POST['tran_id']
            val_id = request.POST['val_id']
            return HttpResponseRedirect(reverse('purchase', kwargs={'tran_id':tran_id,'val_id':val_id}))
        
        elif status == 'FAILED':
            return redirect('Faild')
        
        elif status == 'CANCEL':
            return redirect('CANCEL')

    return render(request,'payment/complete.html')

def purchase(request,tran_id,val_id):
    order_qs = Order.objects.filter(user=request.user,ordered=False)[0]
    order_qs.ordered = True
    order_qs.paymentId = tran_id
    order_qs.orderId = val_id
    order_qs.save()

    cart_qs = Cart.objects.filter(user=request.user,purchased=False)
    for item in cart_qs:
        item.purchased = True
        item.save()
    

    return redirect('/')

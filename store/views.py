from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)
    page_number = request.GET.get("page")
    product_view = paginator.get_page(page_number)
    context ={
        'product_view':product_view
    }
    return render(request,"index.html",context)

def product_details(request,id):
    product_detail = Product.objects.get(id=id)
    product_related_image = ProductRelatedImage.objects.filter(related_img=product_detail)
    context ={
        'product_detail':product_detail,
        'product_related_image':product_related_image
    }
    return render(request,"product.html",context)

def category_wise_product(request,id):
    cat_obj = Category.objects.get(id=id)
    cat_filter_product = Product.objects.filter(category=cat_obj)
    context = {
        'product_view':cat_filter_product
    }
    return render(request,"index.html",context)


def product_search(request):
    search_item = request.GET.get('search_item')
    search_product_view = Product.objects.filter(name__icontains = search_item)
    context = {
        'search_product_view':search_product_view
    }
    return render(request,"search_product.html",context)

def product_price_search(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    search_product_view = Product.objects.filter(price__range = (min_price,max_price))
    context = {
        'search_product_view':search_product_view
    }
    return render(request,"search_product.html",context)





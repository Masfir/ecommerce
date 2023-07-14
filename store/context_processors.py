from .models import *

def menu(request):
    menu_item = Category.objects.filter(parent=None)
    return dict(menu_item=menu_item)
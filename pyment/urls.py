from django.urls import path
from .views import *
urlpatterns = [
    path('checkout/',checkout,name='checkout'),
    path('complete/',complete,name='complete'),
    # path('purchase/<tran_id>/val_id/',purchase,name='purchase'),
    path('purchase/<tran_id>/<val_id>/',purchase, name="purchase"),
    
]

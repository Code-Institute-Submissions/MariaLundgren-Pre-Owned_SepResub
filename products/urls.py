from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products',),
    path('<product_id>', views.selected_product, name='selected_product'),
]

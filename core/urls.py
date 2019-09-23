
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    ItemDetailView,
    checkout,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_from_cart,
    remove_single_item_from_cart

) 

urlpatterns = [

    # path('',views.index),


    path('', HomeView.as_view(),name='home'),

    path('product/<slug>',ItemDetailView.as_view(),name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('addToCart/<slug>',add_to_cart,name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('checkout/', checkout, name='checkout'),
]


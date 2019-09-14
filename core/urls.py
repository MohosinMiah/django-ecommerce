
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,ItemDetailView


urlpatterns = [

    # path('',views.index),


    path('', HomeView.as_view(),name='home'),

    path('product/<slug>',ItemDetailView.as_view(),name='product'),

    

]


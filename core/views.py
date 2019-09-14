from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Item




# Create your views here.

def home(request):

    

   
    product_items = Item.objects.all()
      
    
    return render(request,'home.html',{'product_items':product_items})
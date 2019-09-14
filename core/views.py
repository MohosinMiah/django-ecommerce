from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Item
from django.views.generic import TemplateView,View,ListView,DetailView
# Create your views here.




class HomeView(ListView):
    model = Item
    context_object_name = 'product_items'
    template_name = 'home.html'

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'product_item'
    template_name = 'product.html'



def home(request):

    

   
    product_items = Item.objects.all()
      
    
    return render(request,'home.html',{'product_items':product_items})
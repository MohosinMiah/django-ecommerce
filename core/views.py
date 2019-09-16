from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,redirect
# from django.shortcuts import redirect
from .models import Item,OrderItem,Order
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView,View,ListView,DetailView
import datetime
# Create your views here.




class HomeView(ListView):
    model = Item
    context_object_name = 'product_items'
    template_name = 'home.html'

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'product_item'
    template_name = 'product.html'


# Add To Cart 

def add_to_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    check_Item = OrderItem.objects.filter(item__slug = item.slug)
    ordered_qs = Order.objects.filter(user = request.user, ordered = False)
    
    try:
       orderItem = OrderItem.objects.get(item__slug = item.slug)
    except OrderItem.DoesNotExist:
        orderItem = None

    if check_Item:
        print("Alrady Exist")
    else:    
        # Solve create() takes 1 positional argument but 2 were given django   using (item = item)
        orderItem = OrderItem.objects.create(item = item)
    

    if ordered_qs.exists():
        order = ordered_qs[0]

        # Check If Order item in the Order
        if order.items.filter(item__slug = item.slug).exists():
            orderItem.quantity += 1
            orderItem.save()
        else:
            if check_Item:
                pass
            else:
                order.items.add(orderItem)   
    else:
        if check_Item:
            pass
        else:
            order = Order.objects.create(user = request.user,ordered_date=datetime.datetime.now())
            order.items.add(orderItem)   


    return redirect("product",slug=slug)    




def home(request):

    

   
    product_items = Item.objects.all()
      
    
    return render(request,'home.html',{'product_items':product_items})
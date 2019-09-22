from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,redirect
# from django.shortcuts import redirect
from .models import Item,OrderItem,Order
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView,View,ListView,DetailView
import datetime
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
# Create your views here.




class HomeView(ListView):
    model = Item
    context_object_name = 'product_items'
    paginate_by = 1
    template_name = 'home.html'

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'product_item'
    template_name = 'product.html'


# Add To Cart 

# def add_to_cart(request,slug):
#     item = get_object_or_404(Item, slug=slug)
#     # Solve create() takes 1 positional argument but 2 were given django   using (item = item)
#     orderItem,create = OrderItem.objects.get_or_create(item = item,user=request.user,ordered=False)
#     ordered_qs = Order.objects.get(user = request.user, ordered = False)

#     if ordered_qs:
#         # order = ordered_qs[0]

#         # Check If Order item in the Order
#         if ordered_qs.items.filter(item__slug = item.slug).exists():
#             orderItem.quantity += 1
#             orderItem.save()
#     else:
#         order = Order.objects.create(user = request.user,ordered_date=datetime.datetime.now())
#         order.items.add(orderItem)   

#     return redirect("product",slug=slug)    


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("product",slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("product",slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("product",slug=slug)



def home(request):

    product_items = Item.objects.all()
      
    
    return render(request,'home.html',{'product_items':product_items})
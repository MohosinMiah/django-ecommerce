from django.contrib import admin
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.




CATEGORY_CHOISE = (
    ('S','Shirt'),
    ('SW','Sport Wear'),
    ('OW','Out Wear')
)


LABEL_CHOISE = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
)


# Create Item Table

class Item(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True,null=True)
    category = models.CharField(choices=CATEGORY_CHOISE,max_length=4)
    label = models.CharField(choices=LABEL_CHOISE,max_length=4)
    slug = models.SlugField()
    description = models.TextField()
    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    
    def add_to_cart(self):
        return reverse("add_to_cart", kwargs={"slug": self.slug})
    



class OrderItem(models.Model):

    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.title



class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    items = models.ManyToManyField(OrderItem)

    start_date = models.DateTimeField(auto_now_add=True)

    ordered_date = models.DateTimeField()

    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username




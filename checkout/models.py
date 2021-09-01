import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from django_countries.fields import CountryField
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=50, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=25, null=True)
    street_address = models.CharField(max_length=50, null=True)
    postcode = models.CharField(max_length=25, null=True)
    town_or_city = models.CharField(max_length=50, null=True)
    country = CountryField(blank_label='Country *', null=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()    


    def update_total(self):
        self.order_total = OrderLineItem
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order.order_number}'

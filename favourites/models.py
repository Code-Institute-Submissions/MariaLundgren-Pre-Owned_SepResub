from django.db import models

from products.models import Product
from django.contrib.auth.models import User


class Favourites(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)

from django.db import models

from products.models import Product
from profiles.models import User


class Favourites (models.Model):
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)

from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Favourites(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

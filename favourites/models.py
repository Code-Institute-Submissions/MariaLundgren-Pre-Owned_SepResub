from django.db import models

from products.models import Product
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Favourites(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_or_update_Favourites(sender, instance, created, **kwargs):

    if created:
        Favourites.objects.create(user=instance)
    instance.favourites.save()
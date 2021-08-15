from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favourite = models.ManyToManyField(UserProfile, related_name='favourite', blank=True)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):

    default_user = models.OneToOneField
    default_email = models.CharField(max_length=50, null=True)
    default_phone_number = models.CharField(max_length=25, null=True)
    default_street_address = models.CharField(max_length=50, null=True)
    default_postcode = models.CharField(max_length=25, null=True)
    default_town_or_city = models.CharField(max_length=50, null=True)
    default_country = CountryField(blank_label='Country *', null=True)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def update_or_create_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)
#    instance.userprofile.save()

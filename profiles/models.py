from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django_countries.fields import CountryField


@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    user_email = instance.email
    username = user_email[:30]
    n = 1
    while User.objects.exclude(pk=instance.pk).filter(
            username=username).exists():
        n += 1
        username = user_email[:(29 - len(str(n)))] + '-' + str(n)
    instance.username = username


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_name = models.CharField(max_length=50,
                                    null=True)
    default_phone_number = models.CharField(max_length=25,
                                            null=True)
    default_street_address = models.CharField(max_length=50,
                                              null=True)
    default_postcode = models.CharField(max_length=25,
                                        null=True)
    default_town_or_city = models.CharField(max_length=50,
                                            null=True)
    default_country = CountryField(blank_label='Country',
                                   null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Contact(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    answer = models.TextField(null=True, blank=True)

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    answer = models.TextField(null=True, blank=True)

from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100, null=False, blank=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    REQUIRED_FIELDS = ["full_name", "email", "address", "phone", "password"]

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.full_name
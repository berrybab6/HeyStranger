from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    email = models.EmailField(max_length=255, blank=False, verbose_name="Email Address")
    profile_url = models.URLField(max_length=526,blank=True, null=True, verbose_name="Profile Url")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.email

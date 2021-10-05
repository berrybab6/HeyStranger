from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.conf import settings

# Create your models here.
class Users(AbstractUser):
    email = models.EmailField(max_length=255, blank=False, verbose_name="Email Address")
    profile_url = models.URLField(max_length=526,blank=True, null=True, verbose_name="Profile Url")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.email
class Comment(models.Model):
    description = models.CharField(max_length=526, null=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_on = models.DateField(auto_now_add=True)
class Secret(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=526, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    posted_on = models.DateField(auto_now=True)
    like = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11)
    mailactivated = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="account/images", null=True, blank=True)

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11)
    mailactivated = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="account/images", null=True, blank=True)
    auth_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_profile_picture(self):
        if self.picture:
            return self.picture.url
        return "/media/account/images/annon.png"
    
    def __str__(self) -> str:
        return self.username
    
    def fullname(self):
        return self.first_name + " " + self.last_name